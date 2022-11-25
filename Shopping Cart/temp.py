import csv


def main():
    with open('shopping.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        labels = []
        evidence = []

        month_dictionary = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}

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

            evidence.append([administrative, administrative_duration, informational, informational_duration, productRelated, productRelated_duration, bounceRates, exitRates, pageValues, specialDay, monthInt, operatingSystem, browser, region, trafficType, visitorType, weekend])

            if line[17] == 'TRUE': 
                labels.append(1)
            else:
                labels.append(0)
        for index, val in enumerate(evidence):
            print(f'{labels[index]} => {val}')
        
        print(len(evidence), len(labels)
        return (evidence, labels)  

main()


