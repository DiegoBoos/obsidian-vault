Positive/Negative —> What I predict
False/True —> Was I right or wrong

| Actual | Prediction | 0   | 1   |     |
| ------ | ---------- | --- | --- | --- |
| **0**  |            | 30  | 15  | 45  |
| **1**  |            | 20  | 25  | 45  |
|        | **Total**  | 50  | 40  | 90  |

**true positives (TP):** A predicted “1”, and actually a “1”.  
In our example, they actually donated.

**true negatives (TN):** A predicted “0”, and actually a “0”.

**false positives (FP):** A predicted “1”, but actually a “0”.  
(aka: Type 1 Error)

**false negatives (FN):** A predicted “0”, but actually a “1”.  
(aka: Type 2 Error)

**Prevalence**
Overall percent of actuals true
$$
\frac{Actual}{Total}
$$
**Accuracy**
All the correct classifications divided by all classifications
$$
\frac{(TP + TN)}{Total}
$$
**Misclassification Rate (aka: Error Rate)**
Percent misclassified
$$
\frac{(FP + FN)}{Total}
$$
**Precision**
How much the model is precise to predict in the positive class

$$
\frac{TP}{(TP + FP)}
$$
**Sensitivity Recall TPR**
How many positives finds on the dataset

$$
\frac{TP}{(TP + FN)}
$$
**Specificity TNR**
How many negatives finds on the dataset

$$
\frac{TN}{(TN + FP)}
$$

**Balanced accuracy**
$$
mean(Sensitivity,Specificity)(1/2)*(.566+667) = 0.611
$$

**Examples:**
**Prevalence:** Overall percent of actual ‘1’s:  
  `Actual ‘1’ / TOTAL = 45/90 = 0.50`

**Accuracy:** The proportion of cases correctly classified:  
  `(TP + TN) / Total = (25 + 30) / 90 = 0.611`

**Misclassification Rate (Error Rate):** Percent misclassified:  
  `(FP + FN) / Total = (15 + 20) / 90 = 0.389`

**Precision:** Percent of predicted ‘1’s that are ‘1’s:  
  `TP / (TP + FP) = 25 / (25 + 15) = 0.625`

**Sensitivity (Recall, True Positive Rate):** Percent of ‘1’s classified as ‘1’:  
  `TP / (TP + FN) = 25 / (25 + 20) = 0.556`

**Specificity (True Negative Rate):** Percent of ‘0’s classified as ‘0’:  
  `TN / (TN + FP) = 30 / (30 + 15) = 0.667`

**Balanced Accuracy:**  
  `mean(Sensitivity, Specificity) = (1/2) * (0.556 + 0.667) = 0.611`