
# Python version of the Outlier Demo

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Outlier_Example.txt")

# Boxplots using default IQR rule
for col in ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x8', 'x9']:
    plt.figure()
    sns.boxplot(x=df[col], orient='h')
    plt.title(f'Boxplot of {col}')
    plt.show()

# Boxplots with adjusted IQR range
for col in ['x1', 'x2']:
    plt.figure()
    sns.boxplot(x=df[col], orient='h', whis=2.0)
    plt.title(f'Boxplot of {col} with IQR*2')
    plt.show()

# Density plots and rugs
for col in ['x6', 'x3']:
    plt.figure()
    sns.kdeplot(df[col], fill=True)
    sns.rugplot(df[col], color='red')
    plt.title(f'Density Plot of {col}')
    plt.show()

# Scatter plots to detect hidden outliers
for col in ['x8', 'x9']:
    plt.figure()
    sns.kdeplot(df[col], fill=True)
    sns.rugplot(df[col], color='red')
    plt.title(f'Density Plot of {col}')
    plt.show()

plt.figure()
plt.scatter(df['x8'], df['x9'])
plt.title('Scatter Plot: x8 vs x9')
plt.xlabel('x8')
plt.ylabel('x9')
plt.show()

# Bar plot for a categorical (factor) variable
df['x7'] = df['x7'].astype('category')
plt.figure()
df['x7'].value_counts().plot(kind='bar')
plt.title('Bar Plot of x7 (Categorical Variable)')
plt.xticks(rotation=45)
plt.show()

# Deleting outliers
df = df[df['x6'] != 0]
plt.figure()
sns.kdeplot(df['x6'], fill=True)
sns.rugplot(df['x6'], color='red')
plt.title('After removing x6 == 0')
plt.show()

# Delete maximum of x2
df = df[df['x2'] != df['x2'].max()]
plt.figure()
sns.kdeplot(df['x2'], fill=True)
sns.rugplot(df['x2'], color='red')
plt.title('After removing max of x2')
plt.show()

# Adjusting extreme value in x3 (replacing min with mean)
min_x3 = df['x3'].min()
df['x3'] = df['x3'].apply(lambda x: df['x3'].mean() if x == min_x3 else x)
plt.figure()
sns.kdeplot(df['x3'], fill=True)
sns.rugplot(df['x3'], color='red')
plt.title('Adjusted x3 (min replaced with mean)')
plt.show()
