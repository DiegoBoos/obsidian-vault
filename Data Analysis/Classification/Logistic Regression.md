Not all variables possess linear correlation

So, instead of 𝑌 = 𝛽0 + 𝛽1𝑋 + 𝜖 we have 𝑌 = 𝛽0 + 𝛽1𝑋 + 𝛽2𝑋2 + ⋯ + 𝛽𝑘𝑋𝑘 + 𝜖

![[Pasted image 20250320093040.png]]

**But, why can’t we classify with MLR?**
Because a binary response variable violates almost all the assumptions of MLR:

- The response (Y) is NOT normally distributed
- The variability of Y is NOT constant
- Variance of Y depends on the expected value of Y
- For a Y~Binomial(n,p) we have Var(Y)=pq which depends on the expected response, E(Y)=p

The model must produce predicted/fitted probabilities that are between 0 and 1

- Linear models produce fitted responses that vary from - ∞ to ∞ Sometimes a binary outcome yields more stable predictions

## Logistic Regression is a Common Classification Technique

- Logistic Regression is a specific application of Generalized Linear Models (GLM)
- GLM were developed to extend linear regression into other settings.
- GLM are characterized by two features:
- A probability distribution or “family” (binomial in the case of logistic)
- A link function mapping the response to the predictors (logit in the case of logistic regression)

**NOTE – There are many, many link functions (logit, probit, inverse, etc) but we will only be looking a one.**

---
The "logit" model:

$$
Y = \ln \left( \frac{p}{1 - p} \right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n + \epsilon
$$
- p is the probability that the event Y occurs, p(Y=1)
- $\frac{p}{1 - p}$ is the "odds ratio".
-  ln $(\frac{p}{1 - p})$ is the log odds ratio, or "logit".
---
### **More:**
- The logistic distribution constrains the estimated probabilities to lie between 0 and 1.

The estimated probability is:
$$
\ln \left( \frac{p}{1 - p} \right) \Rightarrow p = \frac{1}{1 + e^{\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n}} = \frac{1}{1 + e^Y}
$$

- If you let \( Y = 0 \), then \( p = 0.50 \).
- As \( Y \) gets really large, \( p \) approaches 0.
- As \( Y \) gets really small, \( p \) approaches 1.
---
### Assumptions of Logistic Regression

**The dependant variable needs to match the type of regression.**
- Binary logistic regression requires the dependent variable to be binary 
- Ordinal logistic regression requires the dependent variable to be ordinal.

**Independence of Observations.**
- The observations need to be independent of each other. In other words, the observations should not come from repeated measurements or matched data.
- No Multicolinearity
- There should be minimal multicollinearity among the independent variables. That is, the independent variables should not be too highly correlated with each other.

**Independent variables are linearly correlated with the log odds of the dependant variable.**
- It does not require the dependent and independent variables to be linearly related, but the independent variables must be linearly related to the log odds.
- Larger sample size than is typical for MLR
- A general guideline is that you need at minimum of 10 cases with the least frequent outcome for each independent variable in your model. For example, if you have 5 independent variables and the expected probability of your least frequent outcome is .10, then you would need a minimum sample size of 500 (10*5 /.10).

### NOT Assumptions of Logistic Regression

- Logistic regression does NOT require a linear relationship between the dependent and independent variables.
- The error terms (residuals) do not need to be normally distributed.
- Homoscedasticity is of error terms is not required.
- The dependent variable in logistic regression is not measured on an interval or ratio scale.
- The independent variables do not need to be standardized or normally distributed.

**Deviance:** Measure of error
**Null Deviance:** Errors we select if we were randomly select
**Res Deviance:** Has to be lower, this is going to change and useful to compare models
**p-value (z-score):** Analogous from linear regression, how much contribution it makes to the model
**Number of Fisher Scoring iterations:** Check for convergence, less than a hundred is quite common

|                   | Full                   | Vol                | Nbr                                   |
| ----------------- | ---------------------- | ------------------ | ------------------------------------- |
| Converge          | ✅                      | ✅                  | ✅                                     |
| AIC               | 1333.1                 | 1333.7             | 1337                                  |
| Res Dev           | 1321.1                 | 1327.7             | 1327.0                                |
| p-value (z-score) | 1 $5/5$                | 1 $4/4$            | 1 $4/4$                               |
| Coeff             | Vol doesn't make sense | All make sense 4/4 | All the coefficients make sense $4/4$ |
|                   |                        |                    |                                       |
- AIC the less is better
- Residual deviance is lower
- Look at the independent variables, check the expected outcomes to analyze the model further
- If the expected outcome of two variables shows a strong correlation is not good

**Cook's distance**

Observe how influential the datapoint is
We look at the highest observations

![[Pasted image 20250320101222.png]]
In this case the Y axis values are small so there is no much influential datapoints

**Full**

| Actual | Prediction | 0   | 1   |
| ------ | ---------- | --- | --- |
| **0**  |            | 384 | 186 |
| **1**  |            | 167 | 403 |

**Nbr** .5

| Actual | Prediction | 0   | 1   |
| ------ | ---------- | --- | --- |
| **0**  |            | 390 | 180 |
| **1**  |            | 167 | 403 |

**Nbr** .45

| Actual | Prediction | 0   | 1   |
| ------ | ---------- | --- | --- |
| **0**  |            | 332 | 238 |
| **1**  |            | 126 | 444 |
Null deviance, error that explain how far we are from the random guess
Residual deviance, how far we are using the model should be lower than the Null deviance and how much

Ensure the Coefficients fit and we know that by looking at the correlation

**Predictions**

|                                | Full   | Reduced |
| ------------------------------ | ------ | ------- |
| **1. Convergence**             | ✅      | ✅       |
| **2. AIC**                     | 166.48 | 164.98  |
| **3. Residual Dev.**           | 156.48 | 156.98  |
| **4. p-val of Z-Test**         | $3/4$  | $3/3$   |
| **5. Coefficient consistency** | $4/4$  | $3/3$   |
| **Accuracy**                   | .74    | 780     |
| **Sensitivity**                | 74.7   | 787     |
| **Specificity**                | .733   | 773     |
| AUC                            |        | .817    |
| Somers D                       |        | .634    |
FPR  = 1 - TNR (How many of the TN were incorrect)
    = 1 - Specificity

**ROC (Curve for Number GLM)**
The higher the curve, the better the model is in differentiating between the true and false values

**AUC**
0.5: Random
1.0: Perfect Prediction

