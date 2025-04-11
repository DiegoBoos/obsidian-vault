**What is a Neural Network?**
- A **neural network** is a computational model inspired by the human brain.
- It consists of **layers of interconnected nodes (neurons)** used to recognize patterns, relationships, or class boundaries in data.
- Used for **classification**, **regression**, **image recognition**, **language processing**, etc.

**Core Architecture**
1. **Input Layer** – one neuron per feature (predictor variable).
2. **Hidden Layer(s)** – intermediate processing units. You can have one or many.
3. **Output Layer** – produces the final prediction (e.g., class label).

Each **neuron** applies a:
- **Weighted sum of inputs**
- **Activation function** (e.g., sigmoid, ReLU) to introduce non-linearity.

**Training Process (Supervised Learning)**
- The network adjusts weights using **backpropagation**:
    - Calculate **prediction error** (e.g., difference from actual label).
    - **Propagate error backwards** through the network to update weights (gradient descent).
    - **Repeat over many epochs** (iterations through the dataset).

**Hyperparameters to Tune**
- Number of **hidden layers** and **neurons**
- **Learning rate** (controls size of weight updates)
- **Activation functions** (e.g., ReLU, sigmoid, tanh)
- **Epochs** and **batch size**
- **Regularization** to avoid overfitting    

**Advantages**
- **Powerful and flexible** – can model complex non-linear relationships.
- Suitable for **large datasets** with **many features**.
- Can capture **hidden patterns** traditional models may miss.    

**Disadvantages**
- Requires **significant training time**, especially on large data.
- **Overfitting** can occur if the model is too complex or trained too long.
- **Hard to interpret** ("black box").
- **Sensitive to data scaling** – features must be **standardized**.

**Evaluation**
Same metrics as other classifiers:
- **Accuracy**
- **Sensitivity / Recall**
- **Specificity**
- **Precision**
- **Balanced Accuracy**
- **ROC Curve**
- **AUC** and **Somer’s D**

**Common Use Cases**
- Medical diagnosis
- Image recognition
- Fraud detection
- Customer segmentation
- Natural Language Processing (NLP)
