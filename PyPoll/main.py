import os
import csv
os.chdir(os.path.dirname(__file__))
print("route of program is: " + os.getcwd())

csvpath = os.path.join('Resources', 'election_data.csv')

def Average(lst):
    return sum(lst) / len(lst)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    votes_count = 0
    candidate = {}

    for row in csvreader:
        votes_count = votes_count + 1
        if row[2] in candidate:
            candidate[row[2]] = candidate[row[2]] + 1
        else:
            candidate[row[2]] = 1

    output_path = os.path.join("Analysis", "Result.txt")

with open(output_path, 'w') as txtfile:

    line1= txtfile.write("Election Results\n")
    line2 = txtfile.write("--------------------------\n")
    line3 = txtfile.write(f"total votes: {votes_count}\n")
    line4 = txtfile.write("--------------------------\n")
    for key in candidate:
     vote_percentage = (candidate[key]/votes_count)*100
    line = txtfile.write(f"{key}: {vote_percentage:.3f}% ({candidate[key]})\n")
    winner = max(candidate, key=candidate.get)
    line5 = txtfile.write("--------------------------\n")
    line6 = txtfile.write(f"Winner: {winner}\n")
    line7 = txtfile.write("--------------------------\n")