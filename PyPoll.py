# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options/Votes
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidates = ""
winning_counts = 0
winning_percentages = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for rows in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidates_names = rows[2]

        if candidates_names not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidates_names)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidates_names] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidates_names] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end= "")
    
    # After printing final vote count to terminal, save final vote to text file 
    txt_file.write(election_results)

# Determine the percentage of votes for each candidate by looping through counts
# Iterate through the candidate list.
for candidates_names in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidates_names]
    # Calculate the percentage of votes.
    vote_percentages = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes to the Terminal
    print(f"{candidates_names}: {vote_percentages:.1f}% ({votes:,})\n")

# Determine winning vote count and candidate
# Determine if the votes are greater than the winning count.
if (votes > winning_counts) and (vote_percentages > winning_percentages):
     
    # If true then set winning_count = votes and winning_percent =
    # vote_percentage.
    winning_counts = votes
    winning_percentages = vote_percentages
    # Set the winning_candidate equal to the candidate's name
    winning_candidates = candidates_names

    #Print winning candidate results to the terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidates}\n"
    f"Winning Vote Count: {winning_counts:,}\n"
    f"Winning Percentage: {winning_percentages:.1f}%\n"
    f"-------------------------\n")

# Print winning candidate summary to the Terminal
print(winning_candidate_summary)
    