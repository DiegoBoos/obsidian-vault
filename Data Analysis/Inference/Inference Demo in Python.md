## 📥 Load and Explore Data

```python
import pandas as pd

filename = '..data/filename.csv'
df = pd.read_csv(filename)
df.head()
df.describe()
```
## 🧪 One-Sample t-test

```python
from scipy.stats import ttest_1samp

target_column = df.select_dtypes(include='number').columns[0]

t_stat, p_val = ttest_1samp(df[target_column].dropna(), popmean=1200)

print(f"One-sample t-test for {target_column}: t={t_stat:.3f}, p={p_val:.4f}")
```
## 🌊 Density Plots

```python
import matplotlib.pyplot as plt
import seaborn as sns

for col in ['mortality', 'hardness']:
    if col in df.columns:
        plt.figure()
        sns.kdeplot(df[col], fill=True)
        sns.rugplot(df[col], color='red')
        plt.title(f'Density Plot of {col}')
        plt.show()
```
## 📏 Normality Checks with Loops

```python
from scipy.stats import shapiro
import statsmodels.api as sm
import matplotlib.pyplot as plt

numeric_cols = df.select_dtypes(include='number').columns

# Shapiro-Wilk test
for col in numeric_cols:
    stat, p = shapiro(df[col].dropna())
    print(f"Shapiro test for {col}: W={stat:.3f}, p={p:.4f}")

# Q-Q plots
for col in numeric_cols:
    sm.qqplot(df[col].dropna(), line='s')
    plt.title(f"Q-Q Plot for {col}")
    plt.show()
```
## 📊 Boxplots by Group

```python
group_col = "location"
if group_col in df.columns:
    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=df[group_col], y=df[col])
        plt.title(f"{col} by {group_col}")
        plt.show()
```
## 📉 Variance and Group Comparison Tests

```python
from scipy.stats import levene, ttest_ind, mannwhitneyu

groups = df[group_col].dropna().unique()
g1 = df[df[group_col] == groups[0]]
g2 = df[df[group_col] == groups[1]]

for col in numeric_cols:
    print(f"Variance test for {col}")
    print(levene(g1[col].dropna(), g2[col].dropna()))
    print(f"T-test for {col}")
    print(ttest_ind(g1[col].dropna(), g2[col].dropna(), equal_var=True))
    print(f"Mann-Whitney U test for {col}")
    print(mannwhitneyu(g1[col].dropna(), g2[col].dropna(), alternative='two-sided'))
```
## 🔄 Correlation

```python
from scipy.stats import spearmanr

if all(col in df.columns for col in ['hardness', 'mortality']):
    plt.figure()
    sns.scatterplot(x='hardness', y='mortality', data=df)
    plt.title("Hardness vs Mortality")
    plt.show()
    
    corr, p = spearmanr(df['hardness'], df['mortality'])
    print(f"Spearman correlation: r={corr:.3f}, p={p:.4f}")
```
## 🔢 Chi-square Test (for contingency tables)

```python
from scipy.stats import chi2_contingency

# Create a contingency table manually or from dataset
if 'pistonrings' in locals():
    chi2, p, dof, expected = chi2_contingency(pistonrings)
    print("Chi-square Test Result:")
    print(f"Chi2 = {chi2:.3f}, p = {p:.4f}")
    print("Expected Frequencies:")
    print(expected.round(0))
```