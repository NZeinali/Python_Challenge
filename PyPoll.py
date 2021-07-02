
import os
import csv
import operator

#  Defining lists of parameters

candidates=[]
vote_numbers=[]
percent=[]


#  Reading "election_data.csv" file

csv_path=os.path.join("PyPoll/election_data.csv")

with open(csv_path,'r',newline='') as csvdata:
    csvreader=csv.reader(csvdata,delimiter=',')
    csvheader=next(csvreader)  #  Stores the header


#  Sorting the CSV file by the "Candidate" column

    sort=sorted(csvreader,key=operator.itemgetter(2))
    
    
#  Listing the name of candidates & their votes in two separate lists 
   
    count=0
    vote=1
    candidates.append(sort[1][2])
        
    for i in range(1,len(sort)-1):
        vote+=1
        if sort[i][2] != sort[i+1][2]:
            count+=1
            candidates.append(sort[i+1][2])
            vote_numbers.append(vote)
            vote=0
    vote_numbers.append(vote+1)


#  Calculating total number of votes

sum=0
for i in range(len(candidates)):
    sum+=vote_numbers[i]

#  Calculating percentage of candidate's votes & reveals the Winner

winner=candidates[0]  #  Assigns a random winner

for i in range(len(candidates)):
    percent.append('{:.3f}%'.format(vote_numbers[i]/sum*100))

    if vote_numbers[i]>=vote_numbers[0]:
        winner=candidates[i]


#  Printing the results to the terminal

print('---------------------------------')
print("Election Results")
print('---------------------------------')
print(f"Total Votes: {sum}")
print('---------------------------------')

for i in range(len(candidates)):
    print(f"{candidates[i]}:  {percent[i]}  ({vote_numbers[i]})")   

print('---------------------------------')
print(f"Winner: {winner}")
print('---------------------------------')


#  Exporting a text file with the results

csv_path=os.path.join("PyPoll_result.csv")

with open(csv_path,'w',newline='') as result:
    csvwriter=csv.writer(result,delimiter=",")
    
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    
    csvwriter.writerow(['Total Votes: ' + str(sum)])

    csvwriter.writerow(['-------------------------'])
   
    for i in range(len(candidates)):
        csvwriter.writerow([str(candidates[i])+": " + str(percent[i]) + "  (" + str(vote_numbers[i])+")"])

    csvwriter.writerow(['-------------------------'])

    csvwriter.writerow(["Winner: " + winner])

    csvwriter.writerow(['-------------------------'])

