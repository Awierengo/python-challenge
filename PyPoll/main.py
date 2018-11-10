import csv
import os


PollCSV = os.path.join("..\\Resources2","election_data.csv")
# print(PollCSV)
# Read in the CSV file
with open(PollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
   
    votes = []
   
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            votes.append(row[2])
    khan = 0
    correy = 0
    li = 0
    o_tooley = 0

    for v in votes:
        if v = "Khan":
            khan = khan + 1
        elif v = "Correy"

    
    print(header)

    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(len(votes)))
    print("--------------------")
    print("Khan: ")
    print("Correy: ")
    print("Li: ")
    print("O'Tooley: ")
    print("--------------------")
    print("Winner: ")
    