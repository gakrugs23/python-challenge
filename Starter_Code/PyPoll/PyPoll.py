# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results

# Total Votes: 369711
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)

# Winner: Diana DeGette

import os
import csv

# Open election data
with open('election_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    votes = list(readCSV)
    total_votes = len(votes) - 1

# Create an empty dictionary to store candidate votes
candidates = {}
for row in votes[1:]:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] += 1

# Calculate the percentage of votes each candidate received and print the results
with open('election_results.txt', 'w') as file:
    for candidate, vote_count in candidates.items():
        percentage = (vote_count / total_votes) * 100
        result_line = f'{candidate}: {percentage:.3f}% ({vote_count})\n'
        print(result_line)
        file.write(result_line)

    # Find the winner of the election
    winner = max(candidates, key=candidates.get)
    winner_line = f'Winner: {winner}\n'
    print(winner_line)
    file.write(winner_line)

    # Print total number of votes
    total_votes_line = f'Total Votes: {total_votes}\n'
    print(total_votes_line)
    file.write(total_votes_line)

# Inform the user that the results have been exported to 'election_results.txt'
print("Election results have been exported to 'election_results.txt'")
