# Conor Driscoll, Class Lab, 1/30/24
import csv

fNames = []
lNames = []
test1s = []
test2s = []
test3s = []
averages = []

with open("listPractice1.txt") as csvFile:
    data = csv.reader(csvFile)
    # store file data
    for rec in data:
        fNames.append(rec[0])
        lNames.append(rec[1])
        test1s.append(int(rec[2]))
        test2s.append(int(rec[3]))
        test3s.append(int(rec[4]))
        averages.append((int(rec[2]) + int(rec[3]) + int(rec[4])) / 3)
# format
print("FIRST PRINT: INDIVIDUAL VALUES")
print(f"{'First':12} \t{'LAST':12} \t{'TEST1':3} \t{'TEST2':3} \t{'TEST3':3}")
print("---------------------------------------------------------")
# display file data
for i in range(0, len(fNames)):
    print(f"{fNames[i]:12} \t{lNames[i]:12} \t{test1s[i]:3} \t{test2s[i]:3} \t{test3s[i]:3}")

# Gets the lowest grade from the unsorted list
lowAvg = 100
lowUser = ""
for i in range(0, len(averages)):
    if averages[i] < lowAvg:
        lowAvg = averages[i]
        lowUser = fNames[i]



# 2D List
allStudents = []
# Multiple 1D lists --> 1 2D list
for i in range(0, len(fNames)):
    allStudents.append([fNames[i], lNames[i], test1s[i], test2s[i], test3s[i], averages[i]])
# Bubble sort by average
for i in range(0, len(allStudents) - 1):
    for j in range(0, len(allStudents) - i - 1):
        if allStudents[j][5] > allStudents[j + 1][5]:
            allStudents[j], allStudents[j + 1] = allStudents[j + 1], allStudents[j]
print("\nSECOND PRINT: SORTED BY AVERAGE")
print(f"{'First':12} \t{'LAST':12} \t{'TEST1':3} \t{'TEST2':3} \t{'TEST3':3} \t{' AVERAGE':8}")
print("----------------------------------------------------------------")
# Prints all the new sorted values and averages
for student in allStudents:
    print(f"{student[0]:12} \t{student[1]:12} \t{student[2]:3} \t{student[3]:3} \t{student[4]:3} \t{student[5]:8.1f}")
print(f"{lowUser} : {lowAvg:.1f}")
print("\nTHIRD PRINT: LETTER GRADE")
print(f"{'First':12} \t{'LAST':12} \t{'TEST1':3} \t{'TEST2':3} \t{'TEST3':3} \t{' AVERAGE':8} \t{'LETTER AVG':10}")
print("------------------------------------------------------------------------------")
# IF ELIF tree to assign letter grade
for student in allStudents:
    letter = ""
    if student[5] > 90:
        letter = "A"
    elif student[5] > 80:
        letter = "B"
    elif student[5] > 70:
        letter = "C"
    elif student[5] > 60:
        letter = "D"
    else:
        letter = "F"

    print(
        f"{student[0]:12} \t{student[1]:12} \t{student[2]:3} \t{student[3]:3} \t{student[4]:3} \t{student[5]:8.1f} \t    {letter:10}")
