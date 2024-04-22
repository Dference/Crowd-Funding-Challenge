import os
import csv

votes = 0
row_count = 0
cand_list = []
cand_votes = {}
cand_name = []
winner_votes = 0

vote_csv = os.path.join("Resources", "election_data.csv")

# Open the CSV File
with open(vote_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)

# Establish Total Votes
    for row in csvreader:
        votes += 1
        cand_name = row[2]

# Add Candidate Votes
        if cand_name in cand_votes:
            cand_votes[cand_name] += 1
        else:
            cand_votes[cand_name] = 1

# Create Candidate List       
        if cand_name not in cand_list:
            cand_list.append(cand_name)

# Find Vote % 
    for cand_name in cand_list:
        total_votes= cand_votes[cand_name]
        cand_perc =(total_votes/votes) * 100

# Find the Popular Vote
        if total_votes > winner_votes:
            winner = cand_name
            winner_votes = total_votes


# # Export to text file
output_path = os.path.join("Analysis", "Findings.txt")
with open(output_path, "w") as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"----------------------------\n")
    textfile.write(f"Total Votes: {votes}\n")
    textfile.write(f"----------------------------\n")
    for cand_name in cand_list:
        total_votes= cand_votes[cand_name]
        cand_perc =(total_votes/votes) * 100
        textfile.write(f"{cand_name}: {cand_perc:.3f}% ({total_votes})\n")
    textfile.write(f"----------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write(f"----------------------------\n")

# Print All Conclusions
print("Election Results")
print("---------------------")
print(f"Total Votes: {votes}")
print("---------------------")
for cand_name in cand_list:
    total_votes= cand_votes[cand_name]
    cand_perc =(total_votes/votes) * 100
    print(f"{cand_name}: {cand_perc:.3f}% ({total_votes})")
print("----------------------")

print(f"Winner: {winner}")
print("----------------------")





















    





