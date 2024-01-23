#Conor Driscoll Lab 3a
import csv
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
with open("Week 3/Lab/lab3a.csv") as csvFile:
    data = csv.reader(csvFile)
    for rec in data:
        #record adding
        totalRecords += 1
        
        #fancy if-else line
        match rec[0]:
            #treats each case as a new elif statement comparing rec[0] to the case
            case 'D':
                types.append("Desktop")
            case 'L':
                types.append("Laptop")
            case _:
                #default condition - acts as the else statement at the end of the line
                types.append("Other")
        match rec[1]:
            case 'DL':
                brands.append("Dell")
            case 'HP':
                brands.append("HP")
            case 'GW':
                brands.append("Gateway")
            case _:
                brands.append("Other")
        #data appending to each list
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

for i in range(totalRecords):
    #print formatting
    print(
        f"{types[i]:7} \t{brands[i]:7} \t{cpus[i]} \t{rams[i]} \t{disk1s[i]} \t  {hdds[i]} \t{disk2s[i]} \t{systems[i]} \t{years[i]}"
    )
#Prints out final total computers
print(f"\nThere are {totalRecords} computers")


tCompOld = 0
tLapOld = 0
for i in range(totalRecords):
    if(int(years[i]) <= 16):
        if(types[i] == "Desktop"):
            tCompOld += 1
        else:
            tLapOld += 1

print(f"To replace {tCompOld} desktops it will cost ${tCompOld*2000:,}")
print(f"To replace {tLapOld} laptops it will cost ${tLapOld*1500:,}")
print(f"Total cost to replace {tLapOld + tCompOld} computers ${tLapOld*1500 + tCompOld*2000:,}")