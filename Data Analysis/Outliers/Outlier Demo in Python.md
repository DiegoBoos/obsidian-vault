## 📥 Load Dataset

```python
import pandas as pd

filename = '../data/filename.csv'
df = pd.read_csv(filename)
df.head()

```
## 📦 Box Plots using 1.5*_IQR and Adjusted IQR_

```python
import matplotlib.pyplot as plt
import seaborn as sns

numeric_cols = df.select_dtypes(include='number').columns

# Default Boxplots (1.5*IQR)
for col in numeric_cols:
    plt.figure()
    sns.boxplot(x=df[col], orient='h')
    plt.title(f'Boxplot of {col} (1.5*IQR)')
    plt.show()

# Adjusted IQR (range=2)
for col in numeric_cols[:2]:
    plt.figure()
    sns.boxplot(x=df[col], orient='h', whis=2.0)
    plt.title(f'Boxplot of {col} (2*IQR)')
    plt.show()
```
## 🌊 Density Plots

```python
for col in numeric_cols[:2]:
    plt.figure()
    sns.kdeplot(df[col], fill=True)
    sns.rugplot(df[col], color='red')
    plt.title(f'Density Plot of {col}')
    plt.show()
```
## 🔎 Scatter Plot for Hidden Outliers

```python
plt.figure()
plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]], alpha=0.7)
plt.title("Scatter Plot for Outliers")
plt.xlabel(numeric_cols[0])
plt.ylabel(numeric_cols[1])
plt.show()
```
## 🧩 Factor Variables Bar Plot

```python
cat_cols = df.select_dtypes(include='category').columns

for col in cat_cols:
    plt.figure()
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Bar Plot of {col}')
    plt.xticks(rotation=45)
    plt.show()
```