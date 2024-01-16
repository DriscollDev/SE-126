import csv

#initializing counting vars
totalRecords = 0
totalSalaries = 0
#initializing field lists
names = []
ages = []
salaries = []

#opening file to read
with open("Week 2/Demo/example.csv") as csvFile:
    #reading the file and storing data in it
    data = csv.reader(csvFile)
    #iterate through the lines of the csv
    for rec in data:
        #add to total records
        totalRecords+=1

        #store data from file to lists
        names.append(rec[0])#Name
        ages.append(int(rec[1]))#Age
        salaries.append(float(rec[2]))#Salary
        #for each record found in the file
        #display the data values in NEAT columns
        print(f"{rec[0]:10}\t{rec[1]:3}\t${int(rec[2]):,}")
        #add to total
        totalSalaries+= float(rec[2])
#neat print of totals
print(f"TOTAL RECORDS: {totalRecords} | TOTAL SALARY: ${totalSalaries:,}")

#Process List ---> for loop
for i in range(totalRecords):
    #For each value between 0 and the Total amount of Records
    print(f"INDEX: {i}\t {names[i]} is {ages[i]} years old")#and makes ${salaries[i]:,.2f} per year

#Process through the lists to create a total age value
totalAge = 0
for i in range(totalRecords):
    #add each age to a total age variable
    totalAge += ages[i]

#deternmine the average age
averageAge = totalAge/totalRecords
print(f"AVERAGE AGE:{averageAge:.2f}")
