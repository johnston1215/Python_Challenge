#Import modules
import os
import csv

#Create path to raw file
filePath = os.path.join("resources/" + "election_data.csv")

#Read raw CSV file (with)
with open(filePath) as csvFile:
    csvReader = csv.reader(csvFile)

    #Create variables - totalVotes int, candidateList = {candidate: votes}
    totalVotes = 0
    candidateList = []
    candidatevotelist = []
    next(csvReader, None)

    #for each row
    for row in csvReader:
        totalVotes = totalVotes + 1

        #Identify a new candidate
        #if candidateList.index(row[2]) < 0:
        #    candidateList.append(row[2])
        #    candidatevotelist.append(1)
            #else:
            #    candidatevotelist[candidateList.index(row[2])] += 1
    #create temp variables
    
    #For candidate in the list

    #   find one with most votes ( accumulator? )
    #   calc and print percentage

    #Write data to text file
    with open("Analysis/" + "PyPollAnalysis.txt", "w") as out_file:
        out_file.write("Election Results\n")
        out_file.write("----------------\n")
        out_file.write(f"Total Votes: " + str(totalVotes))
        out_file.write("\n----------------")

    #print output
    print("Election Results")
    print("----------------")
    print(f"Total Votes: " + str(totalVotes))
    print("----------------")