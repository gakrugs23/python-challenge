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

# import the os module
import os

# import csv file
import csv

#  open election data
with open('election_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    votes = list(readCSV)
    total_votes = len(votes) - 1

# create an empty dictionary. Iterate over each row in the votes list. If candidate's name is not already a key in the candidates dictionary, add value of 1
# If candidate's name is key in the dictionary, we add its value by 1
# total number of votes each candidate received
    
candidates = {}
for row in votes[1:]:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] +=1

# Calculate the percentage of votes each candidate received. Print candidates name and their percentage of votes (per answer in homeowrk it should be 3 decimal places)
# print total vote count
for candidate, vote_count in candidates.items():
    percentage = (vote_count / total_votes) * 100
    print(f'{candidate}: {percentage: .3f}% ({vote_count})')

# Find winner of the election
winner = max(candidates, key = candidates.get)
print(f'winner: {winner}')

# print total number of votes 
print(f'total votes: {total_votes}')
