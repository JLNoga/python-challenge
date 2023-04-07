#read in the csv
import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

#declare list names
sum_profit = []
dates = []


with open(csvpath) as csvfile:
    
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
        
    for row in csvreader:

#add months to list
        dates.append(row[0]) 

#add profit/loss to list
        sum_profit.append(int(row[1]))

#calculate the total change and then average it and store
    #find the first value
    first = sum_profit[0]
    #find the last value
    last = sum_profit[-1]
    #find the change and average (last minus first)
    average_change = (last - first) / (len(dates) - 1)
    print(float(average_change)) #need to fix to 2 decimals

#find and store the max increase
    great_incr = max(sum_profit)
    
#find and store the max decrease
    great_decr = min(sum_profit)

#print the Financial Analysis Summary
print("Financial Analysis")

print("---------------------------------------------------------------")

print("Total Months: " + str(len(dates)))

print("Net Profit/Loss: " + str(sum(sum_profit)))

print("Average Change: " + str(average_change))

print("Greatest Increase in Profits: " + str(great_incr))

print("Greatest Decrease in Profits: " + str(great_decr))

#Update the PyBank_output text file with Financial Analysis Summary Above
lines = ["Financial Analysis","---------------------------------------------------------------", "Total Months: " + str(len(dates)), "Net Profit/Loss: " + str(sum(sum_profit)), "Average Change: " + str(average_change), "Greatest Increase in Profits: " + str(great_incr), "Greatest Decrease in Profits: " + str(great_decr)]
with open('Analysis/PyBank_output.txt', 'w') as f:
    f.write('\n'.join(lines))
