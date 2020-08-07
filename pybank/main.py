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
    GreatestChange = [monthName, MonthlyChange]
    net_change = 0

    next(csvReader, None)
    for row in csvReader:
        TotalMonths = TotalMonths + 1
    #Get Current profit row[1]
        Total = Total + int(row[1])
    #Calculate the net + / - over the presented timeframe
        if TotalMonths != 1:
            net_change = int(row[1]) - PrevMonth
        PrevMonth = int(row[1])
        MonthlyChange += [net_change]
        monthName += [row[0]]

    #Find greatest period increase in profits over period
        GrtInc = max(MonthlyChange)

    #Find greatest decrease in loss over period
        GrtDec = min(MonthlyChange)
        if MonthlyChange > GreatestChange[1]:
            GreatestChange[1]=MonthlyChange
            GreatestChange[0]=monthName
    #Calculate the average change over periods
    AvgChange = sum(MonthlyChange) / len(MonthlyChange)

    #Print results in terminal window
    #Write data to text file
        
    with open("Analysis/" + "PyBankAnalysis.txt", "w") as out_file:
        out_file.write(f"Greatest Decrease in Profits: " + "str(?????)" + " $" + str(GrtDec))
    print("Financial Analysis")
    print("------------------")
    print(f"Total months: " + str(TotalMonths))
    print(f"Total: $" + str(Total))
    print(f"Average Change: $" + str(AvgChange))
    print(f"Greatest Increase in Profits: " + "str(?????)" + " $" + str(GrtInc))
    print(f"Greatest Decrease in Profits: " + "str(?????)" + " $" + str(GrtDec))