import os
import csv

election_data = os.path.join("election_data.csv")

candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print(f"Total Votes: {str(total_votes)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print(f"Winner: {winning_candidate}")

output = open("output.txt", "w")
line1 = "Election Results"
line2 = str(f"Total Votes: {str(total_votes)}")
output.write('{}\n{}\n'.format(line1, line2))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
    line3 = str(f"Winner: {winning_candidate}")
    output.write('{}\n'.format(line3))