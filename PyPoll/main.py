import csv
import os


PollCSV = os.path.join("..\\Resources2","election_data.csv")
# print(PollCSV)
# Read in the CSV file
with open(PollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

   # Initialize votes list
    votes = []
   
   # Make list of votes excluding header
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            votes.append(row[2])

    # Initialize vote counts
    khan = 0
    correy = 0
    li = 0
    o_tooley = 0

    # Tally votes with list
    for v in votes:
        if v == "Khan":
            khan = khan + 1
        elif v == "Correy":
            correy = correy +1
        elif v == "Li":
            li = li + 1
        elif v== "O'Tooley":
            o_tooley = o_tooley + 1

    # Calculate percentages
    num_votes = len(votes)
    perc_khan = round((khan / num_votes) * 100,3)
    perc_correy = round((correy / num_votes) * 100,3)
    perc_li = round((li / num_votes) * 100,3)
    perc_o_tooley = round((o_tooley/num_votes) * 100,3)

    # Determine winner
    if khan > correy and khan > li and khan > o_tooley:
        winner = "Khan"
    elif correy > li and correy > o_tooley:
        winner = "Correy"
    elif li > o_tooley:
        winner = "Li"
    else:
        winner = "O'Tooley"

    # Print statements for results
    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(num_votes))
    print("--------------------")
    print("Khan: " + str(perc_khan)+"% (" + str(khan)+")")
    print("Correy: " + str(perc_correy) + "% (" + str(correy)+ ")")
    print("Li: " + str(perc_li) + "% (" + str(li) + ")")
    print("O'Tooley: " + str(perc_o_tooley) + "% ("+ str(o_tooley)+ ")")
    print("--------------------")
    print("Winner: " + winner)
    print("--------------------")
