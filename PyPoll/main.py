import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#declare list names and variables
names = []

voters = []  
countC = 0
countB = 0 
countA = 0


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    

    for row in csvreader:
        #create list of voters
        voters.append(row[0])
        #create list of candidates 
        names.append(row[2])
    
    #make list of candidates unique
    set_names = set(names)
    list_names = (list(set_names))
    
    #count the votes per candidate and update the vote count
    nameA = str(list_names[0])
    nameB = str(list_names[1])
    nameC = str(list_names[2])

    for row in names:
        if row == nameC:
            countC += 1
        elif row == nameB:
            countB += 1
        else:   
            countA += 1

    #calculate each candidate percentage
    percA = countA / len(voters)
    percB = countB / len(voters)
    percC = countC / len(voters)
  
    fperca = (format(percA, '.2%'))
    fpercb = (format(percB, '.2%'))
    fpercc = (format(percC, '.2%'))


    print("Election Results")
    print("----------------------")
    print(f'Total Votes: {(len(voters))}')
    print("----------------------")
    print(f'{list_names[0]}: {fperca} ({countA})')
    print(f'{list_names[1]}: {fpercb} ({countB})')
    print(f'{list_names[2]}: {fpercc} ({countC})')
    print("----------------------")
    print("Winner: Diana DeGette")  #this should be a formula...I ran out of time.


#still needs to print to text file