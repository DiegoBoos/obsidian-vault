```Python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.stats import wilcoxon, f_oneway
import seaborn as sns
import matplotlib.pyplot as plt

# Load Seatbelts dataset
from pydataset import data
SB = data('Seatbelts').dropna()
print(SB.head())

# Split into Train and Test sets (80/20)
train, test = train_test_split(SB, test_size=0.2, random_state=8891)

print("Train PetrolPrice mean:", round(train['PetrolPrice'].mean(), 6))
print("Test PetrolPrice mean:", round(test['PetrolPrice'].mean(), 6))

# Wilcoxon Test (use Mann-Whitney U as alternative if sample sizes differ)
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(train['PetrolPrice'], test['PetrolPrice'], alternative='two-sided')
print("Mann-Whitney U test:", stat, p)

# Split into Train/Test/Validation (60/20/20)
temp, vald = train_test_split(SB, test_size=0.2, random_state=1889)
train, test = train_test_split(temp, test_size=0.25, random_state=1889)  # 0.25 of 80% is 20%

# Means
print("Means of PetrolPrice:")
print("Train:", round(train['PetrolPrice'].mean(), 6))
print("Test:", round(test['PetrolPrice'].mean(), 6))
print("Validation:", round(vald['PetrolPrice'].mean(), 6))

# Add group labels
train['samp'] = 'train'
test['samp'] = 'test'
vald['samp'] = 'valid'

# Combine sets
combined = pd.concat([train, test, vald])

# ANOVA to test PetrolPrice differences across groups
anova_result = f_oneway(
    combined[combined['samp'] == 'train']['PetrolPrice'],
    combined[combined['samp'] == 'test']['PetrolPrice'],
    combined[combined['samp'] == 'valid']['PetrolPrice']
)
print("ANOVA result:", anova_result)

# Optional: boxplot visualization
sns.boxplot(x='samp', y='PetrolPrice', data=combined)
plt.title('PetrolPrice by Data Split')
plt.show()
```
