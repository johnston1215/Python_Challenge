#Import modules
import os
import csv

#Create path to raw file
filePath = os.path.join("resources/" + "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#Read raw CSV file (with)
with open(filePath) as csvFile:
    csvReader = csv.reader(csvFile)
    #Count number of months included in data
    #Ditch (next) header row
    TotalMonths = 0
    Total = 0.00
    PrevMonth = 0.00
    MonthlyChange = []
    monthName = []
    next(csvReader, None)
    for row in csvReader:
        TotalMonths = TotalMonths + 1
    #Get Current profit row[1]
        Total = Total + int(row[1])
    #Calculate the net + / - over the presented timeframe
        net_change = int(row[1]) - PrevMonth
        PrevMonth = int(row[1])
        MonthlyChange += [net_change]
        monthName += [row[0]]

    #Find greatest period increase in profits over period
        GreatestChange = [monthName, MonthlyChange]
        if MonthlyChange > GreatestChange[1]:
            GreatestChange[1]=MonthlyChange
            GreatestChange[0]=monthName

    #Find greatest decrease in loss over period
    #GreatestDecrease = 0
    #for change in MonthlyChange:
    #    if change < GreatestDecrease:
    #        change = GreatestDecrease
    #Not sure how to reference the month

    #Calculate the average change over periods
    AvgChange = sum(MonthlyChange) / len(MonthlyChange)

    #Print results in terminal window
    #Write data to text file
    #PyBankAnalysis = os.path.join("analysis/" + "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
    #with open(PyBankAnalysis.txt, "w") as out_file:
    #    out_file.write(OutputString)
    print("Financial Analysis")
    print("------------------")
    print(f"Total months: " + str(TotalMonths))
    print (f"Total: $" + str(Total))
    print(f"Average Change: $" + str(AvgChange))
    #print(f"Greatest Increase in Profits: " + ??? + "$" + ???)
    #print(f"Greatest Decrease in Profits: " + ??? + "$" + ???)

    #print(monthName)
    #print(MonthlyChange)
    #print(GreatestChange)