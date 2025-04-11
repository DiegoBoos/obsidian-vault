```Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, shapiro, levene, chi2_contingency
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.gofplots import qqplot

# Load ANOVA dataset
df = pd.read_csv("PROG8435-ANOVA-Demo.txt", sep=",")
df["Page"] = df["Page"].astype("category")
df["User"] = df["User"].astype("category")

# Boxplots by Page and User
sns.boxplot(x="Page", y="Time", data=df)
plt.title("Time spent on each Page")
plt.show()

sns.boxplot(x="User", y="Time", data=df)
plt.title("Time spent by each User")
plt.show()

# One-way ANOVA by Page
model_page = ols('Time ~ C(Page)', data=df).fit()
anova_page = sm.stats.anova_lm(model_page, typ=2)
print("One-way ANOVA by Page:")
print(anova_page)

# One-way ANOVA by User
model_user = ols('Time ~ C(User)', data=df).fit()
anova_user = sm.stats.anova_lm(model_user, typ=2)
print("One-way ANOVA by User:")
print(anova_user)

# Two-way ANOVA
model_two = ols('Time ~ C(Page) + C(User)', data=df).fit()
anova_two = sm.stats.anova_lm(model_two, typ=2)
print("Two-way ANOVA:")
print(anova_two)

# Load two-way dataset
hours = pd.read_csv("ANOVA-Demo-2.txt")
hours["Camp"] = hours["Camp"].astype("category")
hours["Program"] = hours["Program"].astype("category")

# Two-way ANOVA on hours
model_hours = ols('Hr ~ C(Camp) + C(Program)', data=hours).fit()
anova_hours = sm.stats.anova_lm(model_hours, typ=2)
print("Two-way ANOVA on Hours:")
print(anova_hours)

# Normality check
sns.kdeplot(hours["Hr"], fill=True)
sns.rugplot(hours["Hr"])
plt.title("Density of Hours")
plt.show()

qqplot(hours["Hr"], line='s')
plt.title("Q-Q Plot of Hours")
plt.show()

print("Shapiro test for Hours:", shapiro(hours["Hr"]))

# Variance test between Camps
camp1 = hours[hours["Camp"] == hours["Camp"].unique()[0]]["Hr"]
camp2 = hours[hours["Camp"] == hours["Camp"].unique()[1]]["Hr"]
print("Levene test between Camps:", levene(camp1, camp2))

# Boxplot for interaction
sns.boxplot(x="Camp", y="Hr", hue="Program", data=hours)
plt.title("Hours Spent by Camp and Program")
plt.show()

# Chi-square test
table = pd.crosstab(hours["Camp"], hours["Program"])
chi2, p, dof, expected = chi2_contingency(table)
print("Chi-square test:")
print("Chi2 =", chi2, "p-value =", p)
print("Expected frequencies:\n", np.round(expected, 0))

# Sample practice section
marks = pd.read_csv("SampleMarks.txt")
print(marks.head())
```
