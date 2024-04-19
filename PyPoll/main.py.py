import os
import csv

votes = 0
total = 0
cand_list = []

vote_csv = os.path.join("Resources", "election_data.csv")

# Read the CSV file, find total votes and candidate list
with open(vote_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        votes += 1
        total += int(row[0])
        cand_name = row[2]
        
        if cand_name not in cand_list:
            cand_list.append(cand_name)

print(f"Total {votes}")
for cand_name in cand_list:
    print(cand_name)

# Find the total 


    





