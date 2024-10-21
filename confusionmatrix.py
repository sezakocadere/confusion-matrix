actuals = {"A": [16, 0, 3, 0], "B": [1, 17, 0, 2], "C": [0, 2, 11, 0], "D": [1, 1, 1, 10]}
predicteds = {"A": [16, 1, 0, 1], "B": [0, 17, 2, 1], "C": [3, 0, 11, 1], "D": [0, 2, 0, 10]}


def calculateConfusionMatrixByClassNameAndIndex(className, classIndex):
 actualValues = actuals[className]
 predictedValues = predicteds[className]

 TP = actualValues[classIndex]
 FP = sum(predictedValues) - TP
 FN = sum(actualValues) - TP
 TN = sum(sum(value for i, value in enumerate(actuals[key]) if i != classIndex) 
    for key in actuals if key != className)
 
 accuracy = round((TN + TP) / (TN + TP + FN + FP), 3)
 print("Accuracy for class " + className + ":", accuracy)

 precision = round(TP / (TP + FP), 3)
 print("Precision for class " + className + ":", precision)

 recall = round(TP / (TP + FN), 3)
 print("Recall for class " + className + ":", recall)

 f1Score = 2 * (precision * recall) / (precision + recall)
 print("F1-score for class " + className + ":", f1Score, "\n")


calculateConfusionMatrixByClassNameAndIndex("B", 1)
calculateConfusionMatrixByClassNameAndIndex("D", 3)