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


def validate(vType, string, expected=None):
    if expected is None:
        expected = []
    match vType:
        case "int":
            try:
                val = int(input(string))
                return val
            except ValueError:
                print("Invalid input")
                return validate(type, string, expected)
        case "list":
            choice = input(string)
            if choice in expected:
                return choice
            else:
                print("Invalid input")
                return validate(type, string, expected)
        case _:
            print("*ERROR* VALIDATE FUNCTION MISPARAMETERED")


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


def printAdventures(masterList):
    print(f"{'  ID':5}\t{'Name':10}\t{'Description'}")
    for rec in masterList:
        print(f"{rec[0]:3}\t{rec[1]:10}\t{rec[2]}")
    input("Press enter to return to main menu: ")


def makeTextBlock():
    row = []
    print("Input the text you want to display to the player, pressing enter will input a new line, so if you with to "
          "submit the block you need to enter on a blank line")

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
                clear()
                printAdventures(masterList)
            case "2":
                clear()
                makeAdventure()
            case "3":
                clear()
                editAdventure()
            case "4":
                clear()
                deleteAdventure()
            case "5":
                clear()
                making = False
            case _:
                clear()
                print("Invalid input")
                sleep(0.5)
        clear()
    print("Goodbye")
    sleep(0.5)


main()
