import csv #necessary package for reading the csv file
import os

#Open the CSV file without worrying about closing it manually
file_to_load = 'Resources/election_results.csv' #variable for the file and path
#Assign a variable to the save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

candidate_options = []
candidate_votes = {}
total_votes = 0 #initializing total_votes count

#for announcing/determining winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    for row in file_reader:
        #Add the vote
        total_votes += 1 
        #Getting unique candidate names only
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #establishing unique candidates as keys with 0 votes initially
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#Save the results to a txt file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file.
    txt_file.write(election_results)
    #going through list of candidates
    for candidate_name in candidate_votes:
        #Retrieve votes of candidate
        votes = candidate_votes[candidate_name]
        #convert to percentage of total_votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #printing results for each candidate
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #save results to txt_file
        txt_file.write(candidate_results)

        #checking for winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #printing winner results
    winning_candidate_summary = (f"-------------------------\n" 
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



