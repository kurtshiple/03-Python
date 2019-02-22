#dependencies
import os
import csv
#this is the most effective way of reading in a csv file
csvpath = os.path.join('..','PyBank','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    

    #print(f"CSV_Header = {csv_header}")

    total_months = 0

    net_total = 0

    last_month_profit = 0
    
    changelist = []
    datelist = []
    #This for loop iterates across the rows in the file and calculates
    #total months, the sum of the profits, and finds the change in profits
    #and puts those in a list
    for rows in csvreader:
        total_months = total_months + 1
        net_total = int(rows[1]) + net_total
        profit = int(rows[1])
        date = rows[0]
        change = int(profit) - int(last_month_profit)
        changelist.append(change)
        datelist.append(date)
        last_month_profit = profit

    #This for loop finds the max in the change list
    greatest_gain = 0
    for number in changelist:
        if (number > greatest_gain):
            greatest_gain = number
    #print(greatest_gain)
    #This for loop finds the min in the change list
    greatest_loss = 0
    for number in changelist:
        if (number < greatest_loss):
            greatest_loss = number
    
   
   
    average_change = sum(changelist[1:])/(len(changelist)-1)
    ggindex = changelist.index(greatest_gain)
    glindex = changelist.index(greatest_loss)

   

    print("Financial Analysis")
    print("__________________________________")
    print(f"Total Months:  {total_months}")
    print(f"Total: $ {net_total}")
    print(f"Average Change: $ {round(average_change,2)}")
    print(f"Greatest Increase in Profits:  {datelist[ggindex]} $ {greatest_gain}")
    print(f"Greatest Decrease in Profits:  {datelist[glindex]} $ {greatest_loss}")
    
    with open('mainb.txt','w') as f:
        f.write("Financial Analysis")
        f.write("\n")
        f.write("__________________________________")
        f.write("\n")
        f.write(f"Total Months:  {total_months}")
        f.write("\n")
        f.write(f"Total: $ {net_total}")
        f.write("\n")
        f.write(f"Average Change: $ {round(average_change,2)}")
        f.write("\n")
        f.write(f"Greatest Increase in Profits:  {datelist[ggindex]} $ {greatest_gain}")
        f.write("\n")
        f.write(f"Greatest Decrease in Profits:  {datelist[glindex]} $ {greatest_loss}")

