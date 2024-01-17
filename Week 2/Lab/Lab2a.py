#Conor Driscoll, Lab 2a, 1/16/2024

#Importing csv handler
import csv

#Format Print
print(f"{'Room':15} \tMax \tMin \tOver")
print("--------------------------------------------")

#Initializing Variables to store all the data
totalRecords = 0
rooms = []
mins = []
maxs = []

#File handling
with open("Week 2/Lab/lab2a.csv") as csvFile:
    data = csv.reader(csvFile)
    for rec in data:
        #record adding
        totalRecords += 1
        #data appending to each list
        rooms.append(rec[0])
        maxs.append(int(rec[1]))
        mins.append(int(rec[2]))

#total amount of rooms over cap
overCount = 0
#iterate through all the rooms
for i in range(totalRecords):
    #gets the difference between the max and the current
    over = (maxs[i]-mins[i])
    #checks if they are over cap
    if((over) < 0):
        #if so they add to the total
        overCount+=1
        #and print out the info
        print(f"{rooms[i]:15} \t{maxs[i]} \t{mins[i]} \t{over*-1}")
#Prints out final total datapoints
print(f"\n\nProcessed {totalRecords} records")
print(f"There are {overCount} rooms over the limit")