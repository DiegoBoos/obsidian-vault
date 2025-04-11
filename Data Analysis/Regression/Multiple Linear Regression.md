**Root mean squared error**
- The square root of the average squared error of the regression (this is the most widely used metric to compare regression models). (aka RMSE)

**R-squared**
- The proportion of variance explained by the model, from 0 to 1. (aka coefficient of determination)

**t-statistic**
• The coefficient for a predictor, divided by the standard error of the coefficient, giving a metric to compare the importance of variables in the model.

#### Regression with more than two variables
----
**Thunder Basin Antelope Study**
The data (X1, X2, X3, X4) are for each year.

X1 = spring fawn count/100
X2 = size of adult antelope population/100
X3 = annual precipitation (inches)
X4 = winter severity index
(1=mild, 5 = severe)

----

We built a Model based on the size of the adult antelope population.

𝑆𝑝𝑟𝑖𝑛𝑔 𝐹𝑎𝑤𝑛 𝐶𝑜𝑢𝑛𝑡 $\hat{(Fwn)} = -1.67914 + 0.49753 * 𝐴𝑑𝑢𝑙𝑡s$

What about other variables?

#### Multiple Regression

Models the relationship between the magnitude of one variable and another.

$$Y = 𝛽0 + 𝛽1𝑋1 + 𝛽2𝑋2 + ⋯ + 𝛽𝑛𝑋𝑛$$

**Considerations for Dealing with Outliers**
**Influence**
- Depending on the outlier and the analysis being performed, it can be minimally influential (in which case, it should be retained) or it could be very influential.

**Size of Dataset**
- If the sample is small (e.g. 5% response, total of 150 cases), the outliers could represent a significant portion of the overall data and have useful data. That is, they represent actual patterns.

**Methodology**
- Examine the data gathering techniques for potential systemic sources or error and inaccuracy.

**Explore the Data**
- Will the particular data be central to the outcome? What are the consequences of error?
- How typical is the outlier. Is it so far outside the typical values that it is unlikely to be ever repeated?

**Precedence**
- How has this data pattern been dealt with in the past?

**Spearman vs Pearson**
Use Spearman when the data it is non-parametric and doesn't show a normal distribution.
Use Pearson when the data is normally distributed and numeric

We are also looking for linear dependencies between each of the independent variables (which would violate one of the assumptions of MLR).

**Assignment 4:** Use Linear Regression to describe the amount of pounds of steam produced every month in the factory
- Develop two models in Step 3
- Create multivariate model one with backward selection

**Methods of choosing variables**

n (number of variables)
Number of candidate models for 'All possible' $2^n -1$
It depends in the number of variables chosen




$$Prc.mod = \hat{Fwn}= \hat{Bo} + \hat{B1} Prc$$


| Item                                                            | Adlt  | Prc   | Sev   | Adt + Prc | Adt + Sev | Prc + Sev | Adt + Prc + Sev |
| --------------------------------------------------------------- | ----- | ----- | ----- | --------- | --------- | --------- | --------------- |
| F-test (p-val) Tells how. better the model is than random guess | ✅     | ✅     | ✅     | ✅         | ✅         | ✅         | ✅               |
| $R^2Adj$                                                        | 0.86  | 0.83  | 0.47  | 0.88      | 0.8439    | 0.86      | 0.955           |
| Residuals                                                       | ✅     | ✅     | ✅     | ✅         | ✅         | ✅         |                 |
| T-Test(p-val)                                                   | ✅     | ✅     | ✅     | 1 $0/2$   | 0 $1/2$   | 1 $1/2$   | 1 $3/3$         |
| Coefficients                                                    | ✅     | ✅     | ✅     | $3/2$     | $1/2$     | $1/2$     | $2/3$           |
| RMSE (As low as possible, very close to the test and train)     | 0.184 | 0.204 | 0.359 | 0.157     | 0.178     | 0.169     | 0.086           |
| Res = 0                                                         | ✅     | ✅     | ✅     | ✅         | ✅         | ✅         | ✅               |
| Normal Res                                                      | ✅     | ✅     | ✅     | ✅         | ✅         | ✅         | ✅               |
| Variance C                                                      | ✅     | ✅     | ✅     | ✅         | ✅         | ✅         | ✅               |
| Auto Corr                                                       | ❌     | ✅     | ✅     | ✅         | ❌         | ✅         | ✅               |
|                                                                 | inf   |       |       |           | inf(1)    | inf(2)    | inf(2)          |

$R^2Adj$: (How much the model changes, should be higher)
RMSE: (Should be smaller)

Leverage (Beyond the rest of the data)
Influence (Basically the trend the data follows ---- lines)

$R^2$ As you add more variables it will go up
$R^2Adj$ penalizations when having extra variables, and all the variables have to contribute in somehow

Cost: associated for extra variables

----
Forward selection: Start with nothing and slightly build the full model

***Step 1***$$\hat{Fwn} = \hat{Bo} = AIC = 500$$
***Step 2***$$\hat{Fwn} = \hat{Bo} + Adult$$$$\hat{Fwn} = \hat{Bo} + Precipitation$$$$\hat{Fwn} = \hat{Bo} + Severity$$$$\hat{Fwn} = \hat{Bo} + Precipitation$$***Step 3***$$\hat{Fwn} = \hat{Bo} + \hat{B1} Precipitation + \hat{B2} Adult$$
**Backward selection:** Start with the full model and keep of removing or decompose

| Item                                                            | Full     | Back    | Fwd      | Step    |
| --------------------------------------------------------------- | -------- | ------- | -------- | ------- |
| F-test (p-val) Tells how. better the model is than random guess | ✅        | ✅       | ✅        | ✅       |
| $R^2Adj$                                                        | 0.768    | 0.768   | 0.766    | 0.764   |
| Residuals                                                       | ✅        | ✅       | ✅        | ✅       |
| T-Test(p-val)                                                   | 1  $5/6$ | 1 $5/6$ | 1  $3/4$ | 1 $3/3$ |
| Coefficients                                                    | $4/5$    | $4/5$   | $3/4$    | $3/3$   |
| RMSE train                                                      | 1.07     | 1.07    | 1.09     | 1.09    |
| RMSE test                                                       |          | 1.22    | 1.20     | 1.21    |
| Normal                                                          |          | ~ ✅     | ~ ✅      |         |
| Mean = 0                                                        |          | ✅       | ✅        |         |
| Variance Const                                                  |          | ✅       | ✅        |         |
| No Auto Correlation                                             |          | ✅       | ✅        |         |
| Inf/Lev                                                         |          | none    | none     |         |



| Item                                                            | Model 1 Train |
| --------------------------------------------------------------- | ------------- |
| F-test (p-val) Tells how. better the model is than random guess | ✅             |
| $R^2Adj$                                                        | 0.1894        |
| Residuals                                                       | ✅             |
| T-Test(p-val)                                                   | ✅             |
| Coefficients                                                    | ✅             |
| RMSE (As low as possible, very close to the test and train)     | 0.184         |
| Res = 0                                                         | ✅             |
| Normal Res                                                      | ✅             |
| Variance C                                                      | ✅             |
| Auto Corr                                                       | ❌             |
|                                                                 | inf           |
- x1 = 3.5
- x2 = -7
- x3 = 12

$$
\hat{y} = 0-18460 + 3.79607 * 3.5
				  + 3.18793 * -7
				  + 1.02718 * 12
$$