#Add our dependencies.
import csv
import os

# Assign variables to load/save a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("hi")


#Write down the names of all the candidates.

#Add a vote count for each candidate.

#Get the total votes for each candidate.

#Get the total votes cast for the election.


