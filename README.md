
# Multi-Class Classification Metrics Calculation
## Problem Statement
The dataset contains 4 classes: **A**, **B**, **C**, **D**. Given the confusion matrix below, write a Python program to calculate the **accuracy**, **precision**, **recall**, and **F1-score** for **Class B** and **Class D**.



### Confusion Matrix

| Classes | Pred A | Pred B | Pred C | Pred D |
|---------|--------|--------|--------|--------|
| **A**   | 16     | 0      | 3      | 0      |
| **B**   | 1      | 17     | 0      | 2      |
| **C**   | 0      | 2      | 11     | 0      |
| **D**   | 1      | 1      | 1      | 10     |


## Explanation
### Metric Definitions:
* **True Positives (TP)**: Correctly predicted instances of a class.
* **False Positives (FP)**: Incorrectly predicted instances as a class.
* **False Negatives (FN)**: Actual instances of the class that were not predicted.
* **True Negatives (TN)**: Correctly predicted instances that are not the class.

### Metric Formulas

1. **Accuracy**: 
   Accuracy = (TP + TN) / (TP + TN + FP + FN)

2. **Precision**: 
   Precision = TP / (TP + FP)

3. **Recall**: 
   Recall = TP / (TP + FN)

4. **F1 Score**: 
   F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
