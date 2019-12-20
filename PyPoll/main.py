import os
import csv

#create empty list
Votes = []
Candidates = []
KhanCount = 0
CorreyCount = 0
OTooleyCount = 0
LiCount = 0

#set path
csvpath = os.path.join(".", "election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    i = 0
    for row in csvreader: 
        
        #create a list of candidates voted for
        Votes.append(row[2])
        
        #Tally individual candidate votes
        if row[2] == 'Khan':
            KhanCount = KhanCount + 1
        elif row[2] == 'Correy':
            CorreyCount = CorreyCount + 1
        elif row[2] == "O'Tooley":
            OTooleyCount = OTooleyCount + 1
        elif row[2] == 'Li':
            LiCount = LiCount + 1


        i = i + 1
#  Find the total number of votes cast

print(f"Total votes: {csvreader.line_num}")

#  Set Aa complete list of candidates who received votes
CandidatesSet = set(Votes)
Candidates = list(CandidatesSet)

#   * Print the percentage of votes each candidate won
print(f"Khan: {round(((KhanCount / csvreader.line_num) * 100), 3)}% ({KhanCount})")
print(f"Correy: {round(((CorreyCount / csvreader.line_num) * 100), 3)}% ({CorreyCount})")
print(f"Li: {round(((LiCount / csvreader.line_num) * 100), 3)}% ({LiCount})")
print(f"O'Tooley: {round(((OTooleyCount / csvreader.line_num) * 100), 3)}% ({OTooleyCount})")

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan