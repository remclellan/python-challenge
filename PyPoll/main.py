import os
import csv
import sys

file = os.path.join("..","Resources","election_data.csv")

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)


print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------")
print(f"Khan: ${total_PL}")
print(f"Correy: ${average_PL}")
print(f"Li: {greatest_increase}")
print(f"O'Tooley: {greatest_decrease}")
print("-----------------------------------")
print(f"Winner: {total_votes}")
print("-----------------------------------")

with open("election_output.txt","w") as f:
    print("Election Results", file=f)
    print("-----------------------------------",file=f)
    print(f"Total Votes: {total_votes}",file=f)
    print("-----------------------------------",file=f)
    print(f"Khan: ${total_PL}",file=f)
    print(f"Correy: ${average_PL}",file=f)
    print(f"Li: {greatest_increase}",file=f)
    print(f"O'Tooley: {greatest_decrease}",file=f)
    print("-----------------------------------",file=f)
    print(f"Winner: {total_votes}",file=f)
    print("-----------------------------------",file=f)