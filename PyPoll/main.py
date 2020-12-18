# Import modules
import os
import csv

# CSV path to collect data
csvpath = os.path.join('..', 'PyPoll','Resources','election_data.csv')

# Initiate total vote count and cadidate list
total_votes = 0
candidate = []

# Read through each row after header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Loop through each row of data to increment vote count and push to candidate array
    for row in csvreader:
        total_votes += 1
        candidate.append(row[2])

# Create dictionary for the number of votes per candidate
candidate_count = dict((i,candidate.count(i)) for i in set(candidate))
# Get winner with max value within dictionary 
winner = max(candidate_count, key=candidate_count.get)

# Print analysis output and export to textfile
output_path = os.path.join('..', 'PyPoll', 'Analysis', 'poll_output.txt')
with open(output_path, "w") as f:
    f.write(f"Election Results\n")
    f.write("-------------------------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------------------------\n")
    for key in candidate_count: 
        f.write(f"{key}: {(candidate_count[key]/total_votes):.3%} ({candidate_count[key]})\n")
    f.write("-------------------------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------------------------\n")



    
   
