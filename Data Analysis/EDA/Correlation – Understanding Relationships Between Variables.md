## 🔍 What is Correlation?

**Correlation** measures the **strength and direction of a relationship** between two **numerical (continuous)** variables. It helps you answer:

> _"When one variable changes, does the other tend to change in a consistent way?"_

⚠️ **Important:** Correlation shows **association**, **not causation**.
## 🔁 Types of Correlation

| Type         | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| **Positive** | As X increases, Y tends to increase (e.g., height vs. weight).            |
| **Negative** | As X increases, Y tends to decrease (e.g., temperature vs. coffee sales). |
| **None**     | No consistent pattern between X and Y.                                    |
Visualize correlation using a **scatter plot**, where each point represents one pair of values (X, Y).
## 📊 Use Cases of Correlation

- **Prediction**: Estimate one variable from another.
    
- **Verification**: Check theories or hypotheses about relationships.
    
- **Precision Testing**: Evaluate reliability of measurement tools.
    
- **Causality Exploration**: Explore if a relationship might exist (but not prove it).
    
- **Modeling Foundation**: Many ML algorithms rely on correlation structures.
## 🧮 Correlation Coefficient (𝑟)

The most common correlation metric is the **Pearson correlation coefficient**, which ranges from **−1 to +1**:

| Value of 𝑟    | Interpretation                      |
| -------------- | ----------------------------------- |
| 1.0            | Perfect positive correlation        |
| 0.7 to 0.99    | Strong positive linear relationship |
| 0.5 to 0.69    | Moderate positive relationship      |
| 0.25 to 0.49   | Weak positive relationship          |
| 0.0 to 0.24    | Almost no linear relationship       |
| −1.0           | Perfect negative correlation        |
| −0.7 to −0.99  | Strong negative linear relationship |
| −0.5 to −0.69  | Moderate negative relationship      |
| −0.25 to −0.49 | Weak negative relationship          |
| −0.0 to −0.24  | Almost no linear relationship       |
## 🔄 Pearson vs Spearman Correlation

| Method       | Best For                                    | Characteristics                           |
| ------------ | ------------------------------------------- | ----------------------------------------- |
| **Pearson**  | Linearly related, normally distributed data | Sensitive to outliers                     |
| **Spearman** | Ranked or non-parametric (ordinal) data     | More robust to outliers, monotonic trends |
## 🧪 How is Correlation Calculated?

### Pearson Formula:
$$r=cov(X,Y)σX⋅σYr = \frac{\text{cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$$Where:
- **cov(X, Y)** = covariance between X and Y
    
- **σX, σY** = standard deviations of X and Y
## 📋 Example: Four Datasets with Same Correlation

| Dataset | Mean (x, y)  | Std. Dev | Correlation (r) |
| ------- | ------------ | -------- | --------------- |
| 1       | (9.00, 7.50) | 3.32     | 0.82            |
| 2       | (9.00, 7.50) | 3.32     | 0.82            |
| 3       | (9.00, 7.50) | 3.32     | 0.82            |
| 4       | (9.00, 7.50) | 3.32     | 0.82            |
Despite identical summary stats and correlation values, **the data plots look drastically different** — highlighting the **importance of visualizing**!
## 📌 Summary Tips

- Always **visualize** correlations (use scatter plots).
    
- Don't confuse **correlation with causation**.
    
- Use **Pearson** for linear, normal data; **Spearman** for non-normal or ranked data.
    
- Be cautious of **outliers**, they can skew correlation results.