import os
import csv
import sys

file = os.path.join("..","Resources","election_data.csv")

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    total_votes=0
    candidates = []
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

#print(candidates)

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    for row in csvreader:
        if row[2] == candidates[0]:
            if candidates[0] =="Khan":
                khan +=1
            elif candidates[0] == "Correy":
                correy +=1
            elif candidates[0] == "Li":
                li +=1
            elif candidates[0] == "O'Tooley":
                otooley +=1
        elif row[2] == candidates[1]:
            if candidates[1] =="Khan":
                khan +=1
            elif candidates[1] == "Correy":
                correy +=1
            elif candidates[1] == "Li":
                li +=1
            elif candidates[1] == "O'Tooley":
                otooley +=1
        elif row[2] == candidates[2]:
            if candidates[2] =="Khan":
                khan +=1
            elif candidates[2] == "Correy":
                correy +=1
            elif candidates[2] == "Li":
                li +=1
            elif candidates[2] == "O'Tooley":
                otooley +=1 
        elif row[2] == candidates[3]:
            if candidates[3] =="Khan":
                khan +=1
            elif candidates[3] == "Correy":
                correy +=1
            elif candidates[3] == "Li":
                li +=1
            elif candidates[3] == "O'Tooley":
                otooley +=1
if khan > correy and khan > li and khan > otooley:
    winner = "Khan"
elif correy > khan and correy > li and correy > otooley:
    winner = "Correy"
elif li > khan and li > correy and li> otooley:
    winner = "Li"
elif otooley > khan and otooley > correy and otooley > li:
    winner = "O'Tooley"



percent_khan = khan/total_votes
percent_correy = correy/total_votes
percent_li = li/total_votes
percent_otooley = otooley/total_votes



print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------")
print("Khan: "+"{:.3%}".format(percent_khan)+f" ({khan})")
print("Correy: "+"{:.3%}".format(percent_correy)+f" ({correy})")
print("Li: "+"{:.3%}".format(percent_li)+f" ({li})")
print("O'Tooley: "+"{:.3%}".format(percent_otooley)+f" ({otooley})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

with open("election_output.txt","w") as f:
    print("Election Results", file=f)
    print("-----------------------------------",file=f)
    print(f"Total Votes: {total_votes}",file=f)
    print("-----------------------------------",file=f)
    print("Khan: "+"{:.3%}".format(percent_khan)+f" ({khan})",file=f)
    print("Correy: "+"{:.3%}".format(percent_correy)+f" ({correy})",file=f)
    print("Li: "+"{:.3%}".format(percent_li)+f" ({li})",file=f)
    print("O'Tooley: "+"{:.3%}".format(percent_otooley)+f" ({otooley})",file=f)
    print("-----------------------------------",file=f)
    print(f"Winner: {winner}",file=f)
    print("-----------------------------------",file=f)