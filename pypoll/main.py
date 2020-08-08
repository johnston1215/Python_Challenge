#Import modules
import os
import csv

#Create path to raw file
filePath = os.path.join("resources/" + "election_data.csv")

#Read raw CSV file (with)
with open(filePath) as csvFile:
    csvReader = csv.reader(csvFile)

    #Create variables - totalVotes int, candidates
    totalVotes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    #Skip header
    next(csvReader, None)

    #for each row
    for row in csvReader:
        totalVotes = totalVotes + 1

    #Add up votes by candidate
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        else:
            OTooley = OTooley + 1
        
    MaxV = max(Khan, Correy, Li, OTooley)
    if Khan == MaxV:
        Winner = "Khan"
    elif Correy == MaxV:
        Winner = "Correy"
    elif Li == MaxV:
        Winner = "Li"
    else:
        Winner = "OTooley"

    #   Calc and print percentage
    KhanP = round(Khan / totalVotes * 100,2)
    CorreyP = round(Correy / totalVotes * 100,2)
    LiP = round(Li / totalVotes * 100,2)
    OTooleyP = round(OTooley / totalVotes * 100,2)

    # Write data to text file
    with open("Analysis/" + "PyPollAnalysis.txt", "w") as out_file:
        out_file.write("Election Results\n")
        out_file.write("----------------\n")
        out_file.write(f"Total Votes: " + str(totalVotes))
        out_file.write("\n----------------")
        out_file.write("\nKhan: " + str(KhanP) + "%" + " (" + str(Khan) + ")")
        out_file.write("\nCorrey: " + str(CorreyP) + "%" + " (" + str(Correy) + ")")
        out_file.write("\nLi: " + str(LiP) + "%" + " (" + str(Li) + ")")
        out_file.write("\nO'Tooley: " + str(OTooleyP) + "%" + " (" + str(OTooley) + ")")
        out_file.write("\n----------------")
        out_file.write("\nWinner: " + str(Winner))
        out_file.write("\n----------------")

    # #print output
    print("Election Results")
    print("----------------")
    print(f"Total Votes: " + str(totalVotes))
    print("----------------")
    print("Khan: " + str(KhanP) + "%" + " (" + str(Khan) + ")")
    print("Correy: " + str(CorreyP) + "%" + " (" + str(Correy) + ")")
    print("Li: " + str(LiP) + "%" + " (" + str(Li) + ")")
    print("O'Tooley: " + str(OTooleyP) + "%" + " (" + str(OTooley) + ")")
    print("----------------")
    print("Winner: " + str(Winner))
    print("----------------")