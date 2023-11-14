import os 
import csv 
 
# Set path for file 
csvpath = os.path.join("election_data.csv") 
 #using csv module to read data 
Candidates = []
Candidate_Votes = []
#Open file
with open(csvpath) as csvfile: #csv reader specifies delimiter and variable that holds contents 
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader) #Reading the header row
    #print(f"{csv_header}") #This will print out the file headers if needed
    
    #Assign Variables 
    count = 0
    Candidate_total = 0
    candvote1 = 0
    candvote2 = 0
    candvote3 = 0
     
    for row in csv_reader:
        #The total number of votes cast
        count+=1
        #A complete list of candidates who received votes
        #Create a list of Candidates
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Candidate_total+=1
        if row[2] in Candidates[0]:
            candvote1 +=1
        elif row[2] in Candidates[1]:
            candvote2 +=1
        elif row[2] in Candidates[2]:
            candvote3 +=1
    
    #Add the votes to the Cand_Votes List    
    Candidate_Votes.append(candvote1)
    Candidate_Votes.append(candvote2) 
    Candidate_Votes.append(candvote3) 
    
    #The percentage of votes each candidate won
        #percentage = votes/count
    PercVotes = []
    cand1perc = round(((candvote1/count) * 100),3)
    cand2perc = round(((candvote2/count) * 100),3)
    cand3perc = round(((candvote3/count) * 100),3)
    PercVotes.append(cand1perc)
    PercVotes.append(cand2perc)
    PercVotes.append(cand3perc)
    #create winner list
    WinList =[]
    #The winner of the election based on popular vote
    if candvote1 > candvote2 and candvote3:
        winner = Candidates[0]#Will provide the winner's name
        mostvotes = candvote1 #If we wanted to show how many votes the winner has
        win1 = "Y" 
    else: win1 = "N"
    if candvote2 > candvote1 and candvote3:
        winner = Candidates[1]
        mostvotes = candvote2
        win2 = "Y"
    else: win2 = "N"
    if candvote3 > candvote1 and candvote2:
        winner = Candidates[2]
        mostvotes = candvote3
        win3 = "Y"
    else: win3 = "N"
    
    #add winner variable to list    
    WinList.append(win1)
    WinList.append(win2)
    WinList.append(win3)
  
    
    print("Election Results")
    print("")
    print("--------------------------------------")
    print("")
    print(f'Total Votes: {count}')
    print("")
    print("--------------------------------------")
    print(f'Candidates[0]: {cand1perc}% ({candvote1})')
    print("")
    print(f'Candidates[1]: {cand2perc}% ({candvote2})')
    print("")
    print(f'Candidates[2]: {cand3perc}% ({candvote3})')
    print("")
    print("--------------------------------------")
    print("")
    print(f'Winner: {winner}')
    print("")
    print("--------------------------------------")
 
 
cleaned_csv = list(zip(Candidate_Votes, Candidates, PercVotes, WinList)) #create tuple for csv   
    #Export to csv
output_file = os.path.join("Pypoll_results.csv")

with open(output_file, "w", newline = '') as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Total_Votes","Candidate","Percent_of_Vote","Winner"])
     writer.writerows(cleaned_csv) 
    

   

    

    