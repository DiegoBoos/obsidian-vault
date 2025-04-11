**Prediction vs. Explanation vs. Anomaly Detection**

**Prediction**
- Predictive modeling is the process of applying a statistical model or data mining algorithm to data for the purpose of predicting new or future observations. (E.g. the output value (Y ) for new observations given their input values (X).

**Explanation**
- Causal or non-casual explanation and explanatory modeling is the use of statistical models for testing causal explanations.

**Anomaly Detection**
- Identifies unusual or atypical patterns (outliers). E.g.
- Fraud detection in various operating environments
- Intrusion detection (unusual patterns in network traffic – potential hack?)
- Identifying tumors in health imaging (E.g. MRI scans)

Models the relationship between the magnitude of one variable and another.

Y = 𝛽0 + 𝛽1𝑋

**Correlation**
- Measures the strength of the relationship.
- Y and X are interchangable

**Regression**
- Quantifies the relationship
- Y is predicted using the value of X

Correlation Matrix or Scatter Plots to verify coefficients
### **Assumptions**
**Residuals are**
  a) normally distributed (QQ plot)
  b) mean = 0
  c) variance is constant (Residuals Chart)
  d) not auto-correlated (Mean)
$$r ~N(0, 0,\sigma2)$$
**Assessing Regression Models**
1) Check the p-value of the F-Stat for significance.
2) Check the Adjusted R2 value for explanatory power.
3) Check Residuals for symmetry.
4) Check t values for significance.
5) Verify Coefficient estimates for sensibleness
$$Res = y -\hat{y}$$$$Res = Bp - B\hat{p}$$
**Root Mean Squared Error (RMSE)**
Essentially, the RMSE is the square root of the average residuals. That is, typically, how far off are our estimates?

This is the typical measure to compare train and test sets (remember validation?)
$$RMSE = \sqrt{\frac{E(yi-\hat{yi})^2}{n}}$$

**Measuring Model Suitability**

**Check the p-value of the F-Stat.**
- Determines is the model has any explanatory power.

**Check the Adjusted R2 value for explanatory power.**
- Also called Coefficient of Determination. Measures the degree of variation in response accounted for by the model.

**Check Residuals for symmetry.**
- This should be approximate and will be more fully assessed in additional residual analysis.

**Check t values for significance.**
- The null hypothesis is β = 0. Checking to make sure parameter estimates are significant.

**Verify Coefficient/parameter estimates for sensibleness**
- Comparing to logic and observations from the correlation matrix.

**RMSE (Root Mean Squared Error)**
- Gives an absolute measure of deviation of predictions from reality.

$$RMSE = \sqrt{\frac{1}{n}E(actual- predicted)^2}$$
**Glossary of Regression**
**Response**
- The variable we are trying to predict.
- Synonyms: Dependent variable, Y-variable, target, outcome

**Independent variable**
- The variable used to predict the response.
- Synonyms: X-variable, feature, attribute

**Record**
- The vector of predictor and outcome values for a specific individual or case.
- Synonyms: row, case, instance, example

**Intercept**
- The intercept of the regression line—that is, the predicted value when X = 0 .
- Synonyms: b 0 , β 0

**Regression coefficient**
- The slope of the regression line.
- Synonyms: slope, b 1 , β 1 , parameter estimates, weightsGlossary of Regression

**Fitted values**
- The estimates Y obtained from the regression line.
- Synonyms: predicted values

**Residuals**
- The difference between the observed values and the fitted values.
- Synonyms: errors

**Least squares**
- The method of fitting a regression by minimizing the sum of squared residuals.
- Synonyms: ordinary least squares