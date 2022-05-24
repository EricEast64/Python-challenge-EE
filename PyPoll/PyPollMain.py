from datetime import date
import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, 'r') as election_csv:
    csv_reader = csv.reader(election_csv, delimiter=',')
    csv_header = next(csv_reader)
    
    voterID = []
    county = []
    candidates = []

    for row in csv_reader:
        voterID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    total_votes = len(voterID)

    uniquecandidates = []
    # traverse the list
    for candidate in candidates:
   # check unique valueis present or not and append
        if candidate not in uniquecandidates:
            uniquecandidates.append(candidate)

    Khan_votes = []
    Correy_votes = []
    Li_votes = []
    OTooley_votes = []

    for row in csv_reader:
        if row[2] == "Khan":
            Khan_votes.append(row[0])
        if row[2] == 'Correy':
            Correy_votes.append(row[0])
        if row[2] == 'Li':
            Li_votes.append(row[0])
        if row[2] == "O'Tooley":
            OTooley_votes.append(row[0])

    Khan_share = (len(Khan_votes) / total_votes) * 100
    Correy_share = (len(Correy_votes) / total_votes) * 100
    Li_share = (len(Li_votes) / total_votes) * 100
    OTooley_share = (len(OTooley_votes) / total_votes) * 100


    print(f"Total Votes: {total_votes}")
    print(f"Unique Candidates: {uniquecandidates}")
    print(f"Khan: {Khan_share}%")
    print(f"Correy: {Correy_share}%")
    print(f"Li: {Li_share}%")
    print(f"O'Tooley: {OTooley_share}%")

    with open("PyPoll.txt", "w") as f:
        f.write("OUTPUT")
    