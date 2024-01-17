#Conor Driscoll, Lab 2b, 1/16/2024

#Importing csv handler
import csv

#Format Print
print(f"Type \tBrand \tCPU \tRAM \tDisk 1 \tNo.HDD \tDisk 2 \tOS \tYR")
print("----------------------------------------------------------------------------")

#Initializing Variables to store all the data
totalRecords = 0
types = []
brands = []
cpus = []
rams = []
disk1s = []
hdds = []
disk2s = []
systems = []
years = []

#File handling
with open("Week 2/Lab/lab2b.csv") as csvFile:
    data = csv.reader(csvFile)
    for rec in data:
        #record adding
        totalRecords += 1
        #data appending to each list
        types.append(rec[0])
        brands.append(rec[1])
        cpus.append(rec[2])
        rams.append(rec[3])
        disk1s.append(rec[4])
        hdds.append(rec[5])
        #Checks if the computer has 2 drives to make sure the data is correctly stored
        if(rec[5] == "2"):
            disk2s.append(rec[6])
            systems.append(rec[7])
            years.append(rec[8])
        else:
            disk2s.append(" ")
            systems.append(rec[6])
            years.append(rec[7])
        


#iterate through all the computers
for i in range(totalRecords):
    #print formatting
    print(
        f"{types[i]} \t{brands[i]} \t{cpus[i]} \t{rams[i]} \t{disk1s[i]} \t  {hdds[i]} \t{disk2s[i]} \t{systems[i]} \t{years[i]}"
    )
#Prints out final total computers
print(f"\nThere are {totalRecords} computers")