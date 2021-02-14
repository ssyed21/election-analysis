#Add our dependencies.
import csv
import os

# Assign variables to load/save a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#declare variables
total_votes = 0
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

winning_candidate = ""
winning_count = 0
winning_percentage = 0

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         winning_count = votes
         winning_percentage = vote_percentage
         winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Total votes is %s" %total_votes)


