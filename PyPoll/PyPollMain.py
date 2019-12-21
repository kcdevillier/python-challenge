import os
import csv
import numpy

#create empty list
Votes = []
Candidates = []
CandidateCount = []
CandidateDict = {}
KhanCount = 0
CorreyCount = 0
OTooleyCount = 0
LiCount = 0

#set path
csvpath = os.path.join(".", "election_data.csv")
output_path = os.path.join(".", "new_election_data.txt")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader: 
        
        #create a list of candidates voted for
        Candidates.append(row[2])
        
        #Tally individual candidate votes
        if row[2] == 'Khan':
            KhanCount = KhanCount + 1
        elif row[2] == 'Correy':
            CorreyCount = CorreyCount + 1
        elif row[2] == "O'Tooley":
            OTooleyCount = OTooleyCount + 1
        elif row[2] == 'Li':
            LiCount = LiCount + 1

#create a max function to find winner candidate
def max(CandidateCount):
    max_ = CandidateCount[0]
    for item in CandidateCount:
        if item > max_:
            max_ = item
    return max_

#Create function that finds percentage for candidates
def CandidatePerc(Count):
    CandidatePerc = round(((Count / csvreader.line_num) * 100), 3) 
    return CandidatePerc

#create a list for candidate counts 
CandidateCount = [CorreyCount, KhanCount, LiCount, OTooleyCount]

#  Set a complete list of candidates who received votes
# alphabatize list so Candidates list and Count list correctly match for dictionary
CandidatesSet = set(Candidates)
CandidatesList = list(CandidatesSet)
CandidatesList.sort()

#Combine list of candidates and counts and find winner
CandidateDict = dict(zip(CandidateCount, CandidatesList))
Winner = CandidateDict[max(CandidateCount)]

#  Print everything 
print("Election Results")
print("----------------------")
print(f"Total votes: {csvreader.line_num}")
print("----------------------")
print(f"Khan: {CandidatePerc(KhanCount)}% ({KhanCount})")
print(f"Correy: {CandidatePerc(CorreyCount)}% ({CorreyCount})")
print(f"Li: {CandidatePerc(LiCount)}% ({LiCount})")
print(f"O'Tooley: {CandidatePerc(OTooleyCount)}% ({OTooleyCount})")
print("---------------------")
print(f"Winner: {Winner}")

#write everything to new text_file
with open(output_path, 'w', newline="") as text_file:

    print("Election Results", file=text_file)
    print("----------------------", file=text_file)
    print(f"Total votes: {csvreader.line_num}", file=text_file)
    print("----------------------", file=text_file)
    print(f"Khan: {CandidatePerc(KhanCount)}% ({KhanCount})", file=text_file)
    print(f"Correy: {CandidatePerc(CorreyCount)}% ({CorreyCount})", file=text_file)
    print(f"Li: {CandidatePerc(LiCount)}% ({LiCount})", file=text_file)
    print(f"O'Tooley: {CandidatePerc(OTooleyCount)}% ({OTooleyCount})", file=text_file)
    print("---------------------", file=text_file)
    print(f"Winner: {Winner}", file=text_file)