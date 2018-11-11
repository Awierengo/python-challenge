import csv
import os


BankCSV = os.path.join("../Resources","budget_data.csv")

# Read in the CSV file
with open(BankCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    
    net_profit = 0
    avg_change = 0
    gr_increase = 0
    inc_index = 0 
    gr_decrease = 0
    dec_index = 0
    difference = 0
    last_month = 0
    difference_list = []
    date_list = []
    diff_total = 0

    # Loop through data separate header
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            # Make a list of dates
            date_list.append(row[0])
            # Total profits after header
            net_profit = net_profit + int(row[1])
            # Sets first month as initial profit, no difference occurs
            if i == 1:
                last_month = int(row[1])
            # Finds difference from previous month, sets new previous month
            else: 
                difference = int(row[1]) - last_month
                difference_list.append(difference)
                last_month = int(row[1])


    zipped_list = zip(date_list, difference_list)

    for index, diff in enumerate(difference_list):
        # Finds total of changes
        diff_total = diff_total + diff
        # Finds greatest increase/decrease index
        if diff > gr_increase:
            gr_increase = diff
            inc_index = index
        elif diff < gr_decrease:
            gr_decrease = diff
            dec_index = index

    # Calculates the Average change  
    avg_change = diff_total / len(difference_list)
    round(avg_change)

    # Print Results 
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(len(date_list)))
    print(f"Total Profits: ${str(net_profit)}")
    print("Average Change: $" + str(round(avg_change,2)))
    print("Greatest Increase : " + date_list[inc_index] + " ($" + str(difference_list[inc_index]) + ")")
    print("Greatest Decrease : " + date_list[dec_index] + " ($" + str(difference_list[dec_index]) + ")")

 #  print("Greatest increase: " + list(zipped_list[inc_index]))
 #  print("Greatest decrease: " + list(zipped_list[dec_index]))
    
    # Save to new file
    f = open('PyBank.txt','w')
    f.write("Financial Analysis\n")
    f.write("------------------\n")
    f.write("Total Months: " + str(len(date_list))+"\n")
    f.write(f"Total Profits: ${str(net_profit)}\n")
    f.write("Average Change: $" + str(round(avg_change,2))+"\n")
    f.write("Greatest Increase : " + date_list[inc_index] + " ($" + str(difference_list[inc_index]) + ")\n")
    f.write("Greatest Decrease : " + date_list[dec_index] + " ($" + str(difference_list[dec_index]) + ")\n")
    f.close()