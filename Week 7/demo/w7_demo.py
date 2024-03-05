import csv
import random
import time

ids = []
lnames = []
fnames = []
class1s = []
class2s = []
class3s = []

with open("w7_demoFile.txt") as csvFile:
    data = csv.reader(csvFile)
    # store file data
    for rec in data:
        ids.append(rec[0])
        lnames.append(rec[1])
        fnames.append(rec[2])
        class1s.append(rec[3])
        class2s.append(rec[4])
        class3s.append(rec[5])

print(f"{'ID':4} \t{'First Name':12} \t{'Last Name':12} \t{'Class 1':7} \t{'Class 2':6} \t{'Class 3':6}")
print("-------------------------------------------------------------------------------------")
for i in range(len(ids)):
    print(f"{ids[i]:4} \t{fnames[i]:12} \t{lnames[i]:12} \t{class1s[i]:7} \t{class2s[i]:7} \t{class3s[i]:7}")

searchName = input("Enter the class name you are looking for\n>").upper()
found = []
for i in range(len(ids)):
    if searchName == class1s[i]:
        found.append(i)
    elif searchName == class2s[i]:
        found.append(i)
    elif searchName == class3s[i]:
        found.append(i)
if found:
    print(f"{'ID':4} \t{'First Name':12} \t{'Last Name':12} \t{'Class 1':7} \t{'Class 2':6} \t{'Class 3':6}")
    print("-------------------------------------------------------------------------------------")
    for rec in found:
        print(
            f"{ids[rec]:4} \t{fnames[rec]:12} \t{lnames[rec]:12} \t{class1s[rec]:7} \t{class2s[rec]:7} \t{class3s[rec]:7}")
else:
    print(f"Sorry, {searchName} was not found in the file")


# Binary Search, ordered list, splits into higher and lower and compares midpoints to the input
def binarySearch(input, orderedList):
    iterations = 0
    low = 0
    high = len(orderedList) - 1
    mid = 0
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if input == orderedList[mid]:
            print(f"Found in {iterations} iterations")
            return mid
        elif input < orderedList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


searchName2 = input("What Last Name are you looking for?\n>").capitalize()
found2 = binarySearch(searchName2, lnames)
if found2 != -1:
    print(f"{'ID':4} \t{'First Name':12} \t{'Last Name':12} \t{'Class 1':7} \t{'Class 2':6} \t{'Class 3':6}")
    print(
        f"{ids[found2]:4} \t{fnames[found2]:12} \t{lnames[found2]:12} \t{class1s[found2]:7} \t{class2s[found2]:7} \t{class3s[found2]:7}")
else:
    print(f"Sorry, {searchName2} was not found in the file")


def bubbleSort(unSortList):
    start = time.time()
    for i in range(len(unSortList) - 1):
        for j in range(len(unSortList) - i - 1):
            if unSortList[j] > unSortList[j + 1]:
                temp = unSortList[j]
                unSortList[j] = unSortList[j + 1]
                unSortList[j + 1] = temp
    end = time.time()
    print(f"Sorted in {end - start} seconds")
    return unSortList


def insertionSort(unSortList):
    start = time.time()
    # iterations = 0
    for i in range(1, len(unSortList)):
        key = unSortList[i]
        j = i - 1
        while j >= 0 and unSortList[j] > key:
            # iterations += 1
            unSortList[j + 1] = unSortList[j]
            j = j - 1
        unSortList[j + 1] = key
    # print(f"Sorted in {iterations} swaps")
    end = time.time()
    print(f"Sorted in {end - start} seconds")
    return unSortList


rand_list = []
rand2 = []
for i in range(1000):
    num = random.randint(1, 1000)
    rand_list.append(num)
    rand2.append(num)

print(f"Random list\t{rand_list}")
print("---------------------------------")
print(f"Bubble Sort\t{bubbleSort(rand_list)}")
print("---------------------------------")
print(f"Insertion Sort\t{insertionSort(rand2)}")
print("---------------------------------")

