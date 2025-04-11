### Bar Plots

```python
for col in df.select_dtypes(include='category'):
    df[col].value_counts().plot(kind='bar', title=col)
    plt.show()
```
### Histograms

```python
for col in df.select_dtypes(include='number'):
    df[col].hist(bins=10)
    plt.title(col)
    plt.show()
```
### Box Plots

```python
for col in df.select_dtypes(include='number'):
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()
```
### Density Plots

```python
for col in df.select_dtypes(include='number'):
    sns.kdeplot(df[col], fill=True)
    sns.rugplot(df[col], color='red')
    plt.title(f"Density Plot of {col}")
    plt.show()
```
### Scatter Plot

```python
if "Income_BDSA" in df.columns and "Unemployment_BDSA" in df.columns:
    plt.scatter(df["Income_BDSA"], df["Unemployment_BDSA"], color='blue', marker='x')
    plt.title("Income vs. Unemployment")
    plt.xlabel("Income")
    plt.ylabel("Unemployment Rate")
    plt.axhline(y=6, color='red', linestyle='--')
    plt.tight_layout()
    plt.show()
```