## What is an Outlier?

An **outlier** is a data point that deviates significantly from other observations. There’s **no single universal definition**, but common views include:

- A value **markedly different** from others in the sample.
- A value that seems to be generated by a **different mechanism** than the rest.
## Why Do Outliers Matter?

1. **Skew Analyses** – Most statistical models are sensitive to outliers.
2. **Reveal Errors** – They may indicate bad data entry or corruption.
3. **Signal Interesting Phenomena** – Sometimes, outliers reveal genuinely interesting anomalies.
## Types of Outliers

|Type|Description|
|---|---|
|**Point**|A single, unusually high or low value (e.g., 999 in an age column).|
|**Contextual**|Normal in one context but abnormal in another (e.g., -2°C in Miami).|
|**Collective**|A group of points that are abnormal together (e.g., cluster of fraud cases).|
## Why Are Outliers Hard to Detect?

- The **boundary between normal and abnormal** is often unclear.
- Different domains require **different similarity or distance measures**.
- **Real-world data is noisy**, making distinction harder.
- Stakeholders often require a **clear justification** for treating data as outliers.
## Methods for Detecting Outliers

| Method               | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| **Statistical**      | Assumes a data distribution and flags observations that don’t fit.          |
| **Proximity-based**  | Measures how isolated a point is from its neighbors.                        |
| **Clustering-based** | Points that don’t belong to any meaningful cluster are considered outliers. |
### Visual Techniques

- **Boxplots**: Show IQR and outliers (commonly using 1.5×IQR rule).
- **Kernel Density Plots**: Highlight subtle distribution anomalies.
- **Scatter Plots**: Useful in bivariate comparisons.
## What Can You Do with Outliers?

| Action      | When to Use                                                   |
| ----------- | ------------------------------------------------------------- |
| **Include** | Preferred if outlier is valid and meaningful.                 |
| **Delete**  | Use only if the value is clearly incorrect or corrupt.        |
| **Adjust**  | Apply when needed for modeling (e.g., time series smoothing). |
