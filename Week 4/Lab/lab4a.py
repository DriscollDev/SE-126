# Conor Driscoll, Lab 4a, 1/30/24
'''
FIELD0     FIELD1    FIELD2  FIELD3    FIELD4
Firstname  Lastname  Age     Nickname  House Allegiance

Process the lists to print them as they appear in the file
Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below)
    Re-Process the lists to print each record fully with the House Mottos
Re-process the lists to find the average age within the list, then
    Print the total number of people in the list
    Print the average age - rounded to a whole number {:.0f}
    Print tallies/final counts for each allegiance (Field4)

House Allegiance | Corresponding Mottos:
-----------------------------------------
House Stark 	 | Winter is Coming
House Baratheon  | Ours is the fury.
House Tully 	 | Family. Duty. Honor.
Night's Watch 	 | And now my watch begins.
House Lannister  | Hear me roar!
House Targaryen  | Fire & Blood
'''

import csv

# Initializing Variables to store all the data
firstNames = []
lastNames = []
ages = []
nicknames = []
houseAllegiances = []

allPeople = []

# File handling
with open("lab4A_GOT_NEW.txt") as csvFile:
    data = csv.reader(csvFile)
    for rec in data:
        # record adding
        firstNames.append(rec[0])
        lastNames.append(rec[1])
        ages.append(int(rec[2]))
        nicknames.append(rec[3])
        houseAllegiances.append(rec[4])

# Printing the data
print(f"{'Firstname':12} \t{'Lastname':12} \t{'Age':3} \t{'Nickname':15} \t{'House Allegiance':15}")
print("----------------------------------------------------------------------------------")
for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:12} \t{lastNames[i]:12} \t{ages[i]:3} \t{nicknames[i]:15} \t{houseAllegiances[i]:15}")

#Iterate through the list and transform them into a 2d list and add on the motto aswell
for i in range(0, len(houseAllegiances)):
    allPeople.append([firstNames[i], lastNames[i], ages[i], nicknames[i], houseAllegiances[i]])
    match houseAllegiances[i]:
        case "House Stark":
            allPeople[i].append("Winter is Coming")
        case "House Baratheon":
            allPeople[i].append("Ours is the fury.")
        case "House Tully":
            allPeople[i].append("Family. Duty. Honor.")
        case "Night's Watch":
            allPeople[i].append("And now my watch begins.")
        case "House Lannister":
            allPeople[i].append("Hear me roar!")
        case "House Targaryen":
            allPeople[i].append("Fire & Blood")
        case _:
            allPeople[i].append("None")

# Printing the data w/ Mottos
print(
    f"\n{'Firstname':12} \t{'Lastname':12} \t{'Age':3} \t{'Nickname':15} \t{'House Allegiance':15} \t{'House Motto':25}")
print("--------------------------------------------------------------------------------------------------------")
for rec in allPeople:
    print(f"{rec[0]:12} \t{rec[1]:12} \t{rec[2]:3} \t{rec[3]:15} \t{rec[4]:15} \t{rec[5]:25}")

#new variables for 3rd print
totalPeople = len(allPeople)
avgAge = sum(ages) / totalPeople
starks = 0
baratheons = 0
tullys = 0
nights = 0
lannisters = 0
targaryens = 0
for rec in allPeople:
    match rec[4]:
        case "House Stark":
            starks += 1
        case "House Baratheon":
            baratheons += 1
        case "House Tully":
            tullys += 1
        case "Night's Watch":
            nights += 1
        case "House Lannister":
            lannisters += 1
        case "House Targaryen":
            targaryens += 1
        case _:
            print("Error")

#Print info for total people, average age, and house allegiances
print(f"\nThere are {totalPeople} characters \nThe average age is {avgAge:.0f}")
print(f"There are {starks} Starks \nThere are {baratheons} Baratheons \nThere are {tullys} Tullys \nThere are {nights} Nights \nThere are {lannisters} Lannisters \nThere are {targaryens} Targaryens")