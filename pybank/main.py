#Import modules
import os
import csv

#Create path to raw file
filePath = os.path.join("resources/" + "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#Read raw CSV file
with open(filePath) as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(row)

#Count number of months included in data
    months = 0
    for row in csvReader:
        months == months + 1
    print(f"Financial results for the last {months} months of data")

#Calculate the net + / - over the presented timeframe
    total = 0
    for row in csvReader:
        total == total + row[1]
    print(f"Net Income/Loss over the presented timeframe is ${total}")

#Calculate the average change over periods
#Create list variable to house changes
    changes = []
    results = row[1]
#find changes for every timeframe and add to changes list
    for row in csvReader:
        results == row[1]-results
        changes.append(results)

#calculate average based on full changes list
#   average = sum(changes) / len(changes)
    print(f"The average change in income/loss over each period is ${average}")
    
#Find greatest period increase in profits over period
    diff = 0
    for row in csvReader:
        monchange == (row[1]-(row-1[1])
        if (monchange>diff):
            diff == monchange
            monchange == 0

#Find greatest decrease in loss over period


#Print results in terminal window


#Export text file with results