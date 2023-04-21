import os 
import csv

poll_file = os.path.join('../Resources/election_data.csv')

count = 0
candidates = []
votes_won = []
votes_won_percent = []
popular_candidate = []

with open (poll_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)


    for row in csvreader:
        count = count + 1
        candidates.append(row[2])

    for x in set (candidates):
        popular_candidate.append(x)

        y = candidates.count(x)
        votes_won.append(y)
        z=(y/count) * 100
        votes_won_percent.append(z)
        
        winner = votes_won.index(max(votes_won))

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(popular_candidate)):
            print(popular_candidate[i] + ": " + str(votes_won_percent[i]) +"% (" + str(votes_won[i])+ ")")
print("-------------------------")
print("The winner is: " + str(winner))
print("-------------------------")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(popular_candidate))):
        text.write(popular_candidate[i] + ": " + str(votes_won_percent[i]) +"% (" + str(votes_won[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + popular_candidate[winner] + "\n")
    text.write("---------------------------------------\n")


