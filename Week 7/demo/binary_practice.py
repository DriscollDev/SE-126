import csv

types = []
names = []
meanings = []
origins = []
allData = []

with open("party.csv", encoding="utf-8") as csvFile:
    data = csv.reader(csvFile)
    for rec in data:
        types.append(rec[0])
        names.append(rec[1])
        meanings.append(rec[2])
        origins.append(rec[3])


def bubbleSort2D(unSortList, sortByIndex):
    for i in range(len(unSortList) - 1):
        for j in range(len(unSortList) - i - 1):
            if unSortList[j][sortByIndex] > unSortList[j + 1][sortByIndex]:
                unSortList[j], unSortList[j + 1] = unSortList[j + 1], unSortList[j]
    return unSortList


def bubbleSort(unSortList):
    for i in range(len(unSortList) - 1):
        for j in range(len(unSortList) - i - 1):
            if unSortList[j] > unSortList[j + 1]:
                unSortList[j], unSortList[j + 1] = unSortList[j + 1], unSortList[j]
    return unSortList


for i in range(len(names)):
    allData.append([types[i], names[i], meanings[i], origins[i]])

print(
    "---------------------------------------------------------------------------------------------")
print(
    "-------------------------------------------UNSORTED------------------------------------------")
print(f"{'Types':10} \t{'Names':12} \t{'Meanings':30} \t{'Origins':7}")
for i in range(len(types)):
    print(f"{types[i]:10} \t{names[i]:12} \t{meanings[i]:30} \t{origins[i]:7}")

allData = bubbleSort2D(allData, 1)
print(
    "---------------------------------------------------------------------------------------------")
print(
    "----------------------------------------SORTED BY NAME---------------------------------------")
print(f"{'Types':10} \t{'Names':12} \t{'Meanings':30} \t{'Origins':7}")
for i in range(len(types)):
    print(f"{allData[i][0]:10} \t{allData[i][1]:12} \t{allData[i][2]:30} \t{allData[i][3]:7}")


allData = bubbleSort2D(allData, 3)
print(
    "---------------------------------------------------------------------------------------------")
print(
    "---------------------------------------SORTED BY ORIGIN--------------------------------------")
print(f"{'Types':10} \t{'Names':12} \t{'Meanings':30} \t{'Origins':7}")
for i in range(len(types)):
    print(f"{allData[i][0]:10} \t{allData[i][1]:12} \t{allData[i][2]:30} \t{allData[i][3]:7}")
