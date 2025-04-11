- **KNN** is a simple yet powerful **classification** (and sometimes regression) algorithm.
- It’s called a **lazy learner** because it doesn’t build a model but makes decisions based on the training data at prediction time.

**Inputs Required**:
- A **feature space** (training data)
- A **distance metric** Euclidean (continuous distribution), Hamming (overlap metric) or Discrete (Boolean metric)
- A **value for k** (number of neighbours)

**Prediction Process**:
- Calculate the distance from the new point to all training points.
- Identify the **k closest** neighbours.
- Assign the class **most common** among those neighbours (or **weighted** by distance, e.g., $w=1/d(generalized linear interpolation)$ or $1/d^2$

 **Choosing the Right k**
- **Too small (e.g., k = 1)**: sensitive to noise.
- **Too large**: may include distant, irrelevant neighbours.
- **Best practice**: Use **odd values** to avoid ties.

**Advantages**
- Simple and easy to implement.
- No assumption about data distribution.
- Flexible (does not involve preprocessing) and effective for **multimodal classes** (classes with multiple clusters).
- Works well when **training data is large and varied**.

 **Disadvantages**
- **Prediction is expensive** – must compute distances to all k-nearest neighbours
- Suffers from the **curse of dimensionality**.
- Accuracy is sensitive to irrelevant or unscaled features – **data should be standardized**.
- May degrade with **noisy or redundant features**.

**Evaluation**
- Works well when measured with:
- **Confusion Matrix**
- **ROC Curve**
- **AUC (Area Under the Curve)** – better if close to 1.
- **Somer’s D**: D=2(AUC−0.5)D = 2(\text{AUC} - 0.5)

**KNN vs. K-Means**

| KNN (Classification)                                                                                              | K-Means (Clustering)                                                             |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Classification Algorithm                                                                                          | Clustering Algorithm                                                             |
| Calculates k nearest data points from<br>data point X. Uses these points to<br>determine which class X belongs to | Uses distance from data points to k-<br>centroids to cluster data into k-groups. |
| “Centroid” is the point X to be classified.                                                                       | Centroids are not necessarily data<br>points.                                    |
| Data point to be classified remains the<br>same.                                                                  | Updates centroid on each pass by<br>calculations over all data in a class.       |
| Only requires k distance calculations.                                                                            | Must iterate over data until center point<br>doesn’t move.                       |
