import csv
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    # # Open & Read The CSV File for the data
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        
        # Skipped the Header of the data
        next(reader)

        # Created two list of labels and evidence 
        labels = []
        evidence = []

        # Created a Month Dictionary of Key -> Month & Value -> Int
        month_dictionary = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}

        # From each reader extract the correct data and their data types
        for line in reader:
        
            administrative = int(line[0])
            administrative_duration = float(line[1])
            informational = int(line[2])
            informational_duration = float(line[3])
            productRelated = int(line[4])
            productRelated_duration = float(line[5])
            bounceRates = float(line[6])
            exitRates = float(line[7])
            pageValues = float(line[8])
            specialDay = float(line[9]) 
            monthInt = int(month_dictionary[line[10]])
            operatingSystem = int(line[11])
            browser = int(line[12])
            region = int(line[13])
            trafficType = int(line[14])

            if line[15] == 'Returning_Visitor': 
                visitorType = 1
            else:
                visitorType = 0
        
            if line[16] == 'TRUE': 
                weekend = 1
            else:
                weekend = 0

            # Append all the data in an evidence list
            evidence.append([administrative, administrative_duration, informational, informational_duration, productRelated, productRelated_duration, bounceRates, exitRates, pageValues, specialDay, monthInt, operatingSystem, browser, region, trafficType, visitorType, weekend])

            # Check to see what label data to append based on the "Revenue"
            if line[17] == 'TRUE': 
                labels.append(1)
            else:
                labels.append(0)

        # Returned a tuple of evidence & labels 
        return (evidence, labels) 

    # raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Created a KNeighborsClassifier of k = 1 model
    k_near_neighbor = KNeighborsClassifier(n_neighbors=1)

    # Retured a fitted k-nearest neighbor model 
    return k_near_neighbor.fit(X=evidence, y=labels)
    # raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # raise NotImplementedError

    # Created 4 Variables -> positive, true_positive, negative, true_negative 
    positive = 0
    true_positive = 0 

    negative = 0
    true_negative = 0

    # Looped through all the predicitions
    for index, pred in enumerate(predictions): 
        
        # Check to see if the prediction was negative
        if pred == 0: 
            negative += 1
            # Check to see if the prediction was the same in the labels
            if labels[index] == pred:
                true_negative += 1
        
        # Check to see if the prediction was positive
        elif pred == 1: 
            positive += 1
            # Check to see if the prediction was the same in the labels
            if labels[index] == pred: 
                true_positive += 1
    
    # Calculated & Return Sensitivity and Specificity
    sensitivity = true_positive / positive
    specificity = true_negative / negative

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
