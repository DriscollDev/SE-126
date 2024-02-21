import csv
from os import system, name


def clear():
    system('cls' if name == 'nt' else 'clear')


ids = []
lNames = []
fNames = []
class1s = []
class2s = []
class3s = []

with open("lab5_students.txt") as csvFile:
    data = csv.reader(csvFile)
    # store file data
    for rec in data:
        ids.append(rec[0])
        lNames.append(rec[1])
        fNames.append(rec[2])
        class1s.append(rec[3])
        class2s.append(rec[4])
        class3s.append(rec[5])


def binarySearch(search, orderedList):
    low = 0
    high = len(orderedList) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if search == orderedList[mid]:
            return mid
        elif search < orderedList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    running = True
    while running:
        clear()
        match input("Welcome!\n1: See All Student Report \n2: Search for a Student [ID]\n3: Search for a Student [Last]\n4: View a Class Roster[class1,class2,class3]\n5: Exit the Program\n>"):
            case "1":
                clear()
                print(
                    f"{'ID':4} \t{'First Name':12} \t{'Last Name':12} \t{'Class 1':7} \t{'Class 2':6} \t{'Class 3':6}")
                print("-------------------------------------------------------------------------------------")
                for i in range(len(ids)):
                    print(
                        f"{ids[i]:4} \t{fNames[i]:12} \t{lNames[i]:12} \t{class1s[i]:7} \t{class2s[i]:7} \t{class3s[i]:7}")
                input(">")
            case "2":
                clear()
                searchID = input("Enter the ID you are looking for\n>").upper()
                found = binarySearch(searchID, ids)
                if found >= 0:
                    print(
                        f"{'ID':4} \t{'First Name':12} \t{'Last Name':12} \t{'Class 1':7} \t{'Class 2':6} \t{'Class 3':6}")
                    print("-------------------------------------------------------------------------------------")
                    print(
                        f"{ids[found]:4} \t{fNames[found]:12} \t{lNames[found]:12} \t{class1s[found]:7} \t{class2s[found]:7} \t{class3s[found]:7}")
                else:
                    clear()
                    print(f"Sorry, {searchID} was not found in the file")
                input(">")
            case "3":
                clear()
                searchName = input("Enter the Last name you are looking for\n>").capitalize()
                found = binarySearch(searchName, lNames)
                if found >= 0:
                    print(
                        f"{'ID':4} \t{'First Name':12} \t{'Last Name':12} \t{'Class 1':7} \t{'Class 2':6} \t{'Class 3':6}")
                    print("-------------------------------------------------------------------------------------")
                    print(
                        f"{ids[found]:4} \t{fNames[found]:12} \t{lNames[found]:12} \t{class1s[found]:7} \t{class2s[found]:7} \t{class3s[found]:7}")
                else:
                    clear()
                    print(f"Sorry, {searchName} was not found in the file")
                input(">")
            case "4":
                clear()
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
                    print(
                        f"{'ID':4} \t{'First Name':12} \t{'Last Name':12}")
                    print("-------------------------------------------------------------------------------------")
                    for index in found:
                        print(
                            f"{ids[index]:4} \t{fNames[index]:12} \t{lNames[index]:12}")
                else:
                    clear()
                    print(f"Sorry, {searchName} was not found in the file")
                input(">")
            case "5":
                running = False
            case _:
                clear()
                print("Invalid Input")
                input(">")
    print("Thank you for using our program. Goodbye")


main()
