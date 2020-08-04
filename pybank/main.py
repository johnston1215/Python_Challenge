#Import modules
import os
import csv

#Create path to raw file
filePath = os.path.join("resources/" + "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#Read raw CSV file (with)
with open(filePath) as csvFile:
    csvReader = csv.reader(csvFile)
    #for row in csvReader:
    #       print(row)

    #Count number of months included in data
    #Ditch (next) header row
    TotalMonths = 0
    Total = 0.00
    MonthlyChange = []
    PrevMonth = 0.00
    next(csvReader, None)
    for row in csvReader:
        TotalMonths = TotalMonths + 1
    #Get Current profit row[1]
        Total = Total + int(row[1])
    #Calculate the net + / - over the presented timeframe
        PrevMonth = int(row[1]) - PrevMonth
        MonthlyChange.append(PrevMonth)
    #Calculate the average change over periods
        AvgChange = sum(MonthlyChange) / len(MonthlyChange)


    #BEN'S CODE----------------------------
    #month_of_change = []
    #net_change_list = []
    #net_change = int(row[1]) - prev_net
        #prev_net = int(row[1])
        #net_change_list += [net_change]
        #month_of_change += [row[0]]
    #net_monthly_avg = sum(net_change_list) / len(net_change_list)


    #Find greatest period increase in profits over period
    GreatestChange = 0
    for change in MonthlyChange:
        if change > GreatestChange:
            change = GreatestChange
    #Not sure how to reference the month
    
    #Find greatest decrease in loss over period
    GreatestDecrease = 0
    for change in MonthlyChange:
        if change < GreatestDecrease:
            change = GreatestDecrease
    #Not sure how to reference the month


    #Print results in terminal window
    print("Financial Analysis")
    print("------------------")
    print(f"Total months " + str(TotalMonths))
    #print (TotalMonths)
    #Print Total
    print (f"Total $" + str(Total))
    #Print Average Change
    print(f"Average Change $" + str(AvgChange))
    #print (AvgChange)

#Write data to text file


#FOR PYPOLL-COPY LATER
#Open File

#Create variables - totalVotes int, candidateList = {candidate: votes}

#Open CSV for read

#for each row
#total votes = totalVotes + 1
#if candidateList.index(current row candidate) < 1:
    #append dict to list and set votes = 0

#increase vote for candidate + 1

#exit for loop

#create temp variables
#For candidate in the list
#   find one with most votes ( accumulator? )
#   calc and print percentage

#print output