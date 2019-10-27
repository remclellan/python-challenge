import os
import csv
import sys

file = os.path.join("..","Resources","budget_data.csv")

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    total_PL=0
    total_months=0
    for row in csvreader:
       total_PL += int(row[1])
       total_months += 1
       #greatest_increase = max(int(column[1].replace(',','')) for column in csvreader)
       #greatest_decrease = min(int(column[1] for column in csvreader)
with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        greatest_increase = max(csvreader, key=lambda row: int(row[1]))

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        greatest_decrease = min(csvreader, key=lambda row: int(row[1]))

average_PL = total_PL/total_months

print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_PL}")
print(f"Average Change: ${average_PL}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")

with open("bank_output.txt","w") as f:
    print("Financial Analysis", file=f)
    print("-----------------------------------",file=f)
    print(f"Total Months: {total_months}",file=f)
    print(f"Total: ${total_PL}",file=f)
    print(f"Average Change: ${average_PL}",file=f)
    print(f"Greatest Increase in Profits: {greatest_increase}",file=f)
    print(f"Greatest Decrease in Profits: {greatest_decrease}",file=f)
