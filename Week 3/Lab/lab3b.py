#Conor Driscoll Lab 3b
import csv

#List inits
totalRecords = 0
idList = []
ageList = []
regList = []
voteList = []
#File handling
with open("Week 3/Lab/voters_202040.csv") as csvFile:
    data = csv.reader(csvFile)
    for rec in data:
        #record adding
        totalRecords += 1
        idList.append(rec[0])
        ageList.append(int(rec[1]))
        regList.append(rec[2])
        voteList.append(rec[3])

#Final Variable Inits
notElig = 0
notReg = 0
notVote = 0
didVote = 0

for i in range(totalRecords):
    #Checks if ineligible
    if(ageList[i]<18):
        notElig+=1
    #if eligible and not registered
    elif(regList[i]=="N"):
        notReg += 1
    #if eligible, registered, and not voted
    elif(voteList[i]=="N"):
        notVote += 1
    #if eligible, registered, and voted
    else:
        didVote += 1

#Prints for final data totals
print(f"{notElig} people were not eligible to vote")
print(f"{notReg} people were eligible but did not register")
print(f"{notVote} people were registered but did not vote")
print(f"{didVote} people voted")
print(f"Processed {totalRecords} records")
    