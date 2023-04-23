
#Get file ready for import.

import os 
import csv

# Set file to variable poll_file

poll_file = os.path.join('../Resources/election_data.csv')

# Create lists

count = 0
candidates = []
votes_won = []
votes_won_percent = []
popular_candidate = []

# Open csv file 

with open (poll_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)


    for row in csvreader:
        
        # Vote count
        count = count + 1

        # Append the 3rd column to candidates list. 
        candidates.append(row[2])

    # Loop that iterates over set of candidates names in candidates list
    for x in set (candidates):

        # Append x to popular_candidate list
        popular_candidate.append(x)

        # Total votes per candidate.
        y = candidates.count(x)
        votes_won.append(y)

        # Percent of total votes for each candidate
        z=(y/count) * 100
        votes_won_percent.append(z)
        
        # Winner 
        winner_vote_count = max(votes_won)
        winner = popular_candidate[votes_won.index(winner_vote_count)]



    # Print results

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes : " + str(count))    
print("-------------------------")

for i in range(len(popular_candidate)):
            print(popular_candidate[i] + ": " + str(votes_won_percent[i]) +"% (" + str(votes_won[i])+ ")")
print("-------------------------")
print("The winner is: " + str(winner))
print("-------------------------")

# Print to a text file: election_results.txt

filename = 'my_election_results.txt'
with open(filename, 'w') as file:
    file.write("Election Results\n")
    file.write("---------------------------------------\n")
    file.write("Total Votes: " + str(count) + "\n")
    file.write("---------------------------------------\n")
    for i, candidate in enumerate(set(popular_candidate)):
        file.write(f"{candidate}: {votes_won_percent[i]:.1f}% ({votes_won[i]})\n")
    file.write("---------------------------------------\n")
    file.write("The winner is: {popular_candidate[winner]}\n")
    file.write("---------------------------------------\n")


