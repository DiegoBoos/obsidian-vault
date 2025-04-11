**Prediction:** Using data (the past or the observed) to prediction (or estimate) the future.

**Simplest Prediction Variables**
- Normally distributed
- Linear relationship

Normal distributions could offer more flexibility, meaning it can be transformed:

- Box-Cox Transformation
- Tukey's Ladder

NOTE: These transformations will not always transform the data into normally distributed data

| Power | Transform | Name              |
| ----- | --------- | ----------------- |
| 2     | $x^2$     | Square            |
| 1     | X         | Original Data     |
| 0     | $logX$    | Logarithm         |
| -1    | $1/X$     | Reciprocal        |
| -2    | $1/X^2$   | Reciprocal Square |
- The Tukey ladder of powers (sometimes called the Bulging Rule) is a way to change the shape of a distribution so that it becomes normal or nearly-normal. It can also help to reduce error variability (heteroscedasticity).

- Note, we don’t have to go by values of 1.

**Accuracy and Precision**

Accuracy is the degree of conformity of a measured or calculated quantity to its actual (true) value.

Precision, also called reproducibility or repeatability, the degree to which further measurements or calculations will show the same or similar results.

***NOTE – This is similar conceptually to ideas of bias and variance.***

![[Pasted image 20250314042856.png]]
![[Pasted image 20250314042939.png]]

**Validation Methods**

Business Reasons
- Need to choose the best model.
- Measure accuracy/power of selected model.
- Good to measure ROI of the modeling project.
- Models are generally used on data we have not seen before.

Statistical Reasons
- Model Building techniques are inherently designed to minimize “loss” or “bias”.
- To an extent, a model will always fit “noise” as well as “signal”.
- If you just fit models on a given dataset and choose the “best” one, it will likely be overly “optimistic”.

**Why Validate?**

1. Because we are making predictions (even when using explanatory power)!
2. Predictions are only useful if they apply to data we have not seen before.

Holdout Validation
- Split the entire dataset in to training, testing, and validation subsets.

Cross Validation
- E.g. Does it make sense that Weight would predict Salary? Perhaps we could use Height:Weight Ratio instead.

![[Pasted image 20250314043559.png]]

**Holdout test set: The naïve approach**

Randomly split the entire dataset into:
- Training set: A dataset used for training the model
- Test set (a.k.a validation set): Data only used for testing the model

**Holdout test set – considerations**

Can the data be split randomly?
- If not, it may lead to underfitting
- Test set and training set should be interchangeable, except for data size

Do we have enough data?
- Example: Guess if a car is American or Japanese based on 50 examples?
- Will the test set be big enough to accurately report our model performance?

The three-way split

**Training set**
- A set of examples used for learning

**Validation set**
- A set of examples used to tune the parameters of a classifier

**Test set**
- A set of examples used only to assess the performance of fully-trained classifier. After assessing the model with the test set, YOU MUST NOT further tune your model (that’s the theory anyway…
- in order to prevent ‘learning the test set’ and ‘overfitting’)

**How to perform the split?**

**How many examples in each data set?**
- Training: Typically 60-80% of data
- Test set: Typically 20-30% of your trained set
- Validation set: Often 20% of data

Examples
- 3 way: Training: 60%, Validation: 20%, Test: 20%
- 2 ways: Training 70%, Test: 30%

**Holdout summary**

**Advantages**
- Intuitive
- Easy to Implement
- Can be done with a completely different dataset if needed.

**Disadvantages**
- Not always possible with small samples
- Could have unfortunate results because of sampling errors

**Cross-Validation**
When we do not have enough data, or have not planned for validation…

**Cross-Validation:**
- Each data point is used both as train and test data.

**Summary:**
- Fit model on 90% of the data; test on remaining 10%.
- Do this on a different 90/10 split.
- Cycle through all 10 cases (or “folds”)

![[Pasted image 20250314054215.png]]