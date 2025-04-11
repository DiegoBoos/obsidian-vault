
# Python version of the Dimensionality Reduction Demo

import pandas as pd
import numpy as np
import time
from scipy.stats import spearmanr
from sklearn.feature_selection import VarianceThreshold
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("PROG8435_Dimension_Data_Demo.csv")

# Initial Spearman correlation timing
start = time.time()
corr_initial, _ = spearmanr(df)
end = time.time()
print("Initial Spearman correlation time:", end - start)

# --- Dimensionality Reduction ---

# 1. Remove columns with excessive missing values (>99% missing)
missing_threshold = 0.99
missing_frac = df.isnull().mean()
cols_to_drop = missing_frac[missing_frac > missing_threshold].index.tolist()
df = df.drop(columns=cols_to_drop)

# 2. Remove low variance features
selector = VarianceThreshold(threshold=0.01)
selector.fit(df.select_dtypes(include=[np.number]))
low_var_cols = df.select_dtypes(include=[np.number]).columns[~selector.get_support()]
df = df.drop(columns=low_var_cols)

# 3. Remove highly correlated features
corr_matrix = df.corr(method="spearman").abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
high_corr_cols = [column for column in upper.columns if any(upper[column] > 0.9)]
df = df.drop(columns=high_corr_cols)

# Encode any non-numeric categorical columns
for col in df.select_dtypes(include=["object", "category"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Final Spearman correlation timing
start = time.time()
corr_reduced, _ = spearmanr(df)
end = time.time()
print("Reduced Spearman correlation time:", end - start)
