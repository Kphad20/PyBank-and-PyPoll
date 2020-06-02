import os
import csv

csvpath = os.path.join('..', 'PyPoll','Resources','election_data.csv')

total_votes = 0
candidate = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate.append(row[2])

candidate_count = dict((i,candidate.count(i)) for i in set(candidate))
winner = max(candidate_count, key=candidate_count.get)

print("Election Results")
print("-------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------")
for key in candidate_count:
    print(f'{key}: {(candidate_count[key]/total_votes):.3%} ({candidate_count[key]})')
print("-------------------------------------------")
print(f'Winner: {winner}')
print("-------------------------------------------")


# Create and print analysis output
output_path = os.path.join('..', 'PyPoll', 'Analysis', 'poll_output.txt')
f = open(output_path, "w")

print("Election Results", file=f)
print("-------------------------------------------", file=f)
print(f'Total Votes: {total_votes}', file=f)
print("-------------------------------------------", file=f)
for key in candidate_count: 
    print(f'{key}: {(candidate_count[key]/total_votes):.3%} ({candidate_count[key]})', file=f)
print("-------------------------------------------", file=f)
print(f'Winner: {winner}', file=f)
print("-------------------------------------------", file=f)

f.close()



    
   
