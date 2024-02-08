# Conor Driscoll 2nd Midterm
import csv
from os import system, name
import random
from time import sleep

"""
Csv per adventure,
each row is new command
first value of each row should be an ID to allow linking

Master List
ID, Name, Description
"""


def clear():
    system('cls' if name == 'nt' else 'clear')


def init():
    adventureLists = []
    with open("masterAdv.csv") as masterAdv:
        tempIDs = []
        tempNames = []
        tempDescriptions = []
        data = csv.reader(masterAdv)
        for rec in data:
            tempIDs.append(int(rec[0]))
            tempNames.append(rec[1])
            tempDescriptions.append(rec[2])
        for i in range(len(tempIDs)):
            adventureLists.append([tempIDs[i], tempNames[i], tempDescriptions[i]])
    return adventureLists


def makeAdventure():
    print("")


def editAdventure(adventure):
    print("")


def deleteAdventure(adventure):
    print("")


def makeTextBlock():
    row = []

    return row


def makeCombatBlock():
    row = []

    return row


def makeSkillBlock():
    row = []

    return row


def main():
    masterList = init()
    making = True
    while making:
        clear()
        print("Welcome to the Dungeon Master Program, what would you like to do")
        match input("1: View List of all Adventures "
                    "\n2: Make a new Adventure "
                    "\n3: Edit an Existing Adventure "
                    "\n4: Delete an existing Adventure "
                    "\n5: Exit the program"
                    "\n>"):
            case "1":
                print(f"{'ID'} {'Name'} {'Description'}")
                for rec in masterList:
                    print(f"{rec[0]} {rec[1]} {rec[2]}")
                print(">")
            case "2":
                makeAdventure()
            case "3":
                editAdventure()
            case "4":
                deleteAdventure()
            case "5":
                making = False
            case _:
                print("Invalid input")
        clear()
    print("Goodbye")
    sleep(2)


main()
