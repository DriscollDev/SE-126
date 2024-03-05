"""
Write a Python program to assign passengers seats in an airplane.Assume a small airplane with seat numbering as follows

Row

1    A B    C D
2    A B    C D
3    A B    C D
4    A B    C D
5    A B    C D
6    A B    C D
7    A B    C D


The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 
1A, 2B and 4C are taken the display should look like this:

Row

1    X B    C D
2    A X    C D
3    A B    C D
4    A B    X D
5    A B    C D
6    A B    C D
7    A B    C D

After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the 
display of available seats is updated.  This continues until all seats are filled or until the user signals that the 
program should end.  If a user types in a seat that is already assigned, the program should say that the seat is 
occupied and ask for another choice. You must use functions that allows the user to enter the row and seat number.  
The row should be asked for separately from the seat number (two inputs) You must use a function that asks the user 
in they want to continue or stop. The function should only accept an uppercase or lowercase y or n

2D List to store all the seat info
first index will be "Row #", "-", "-", "-", "-"
every index after will be "index", "A", "B", "C","D"
taken seats will be changed to an X
Function to handle user input for choosing what seat they want
"""
from os import system, name


def clear():
    system('cls' if name == 'nt' else 'clear')


# Using a loop to add all the data to the list because I am lazy
planeData = [["Row #", "-", "-", "-", "-"]]
for i in range(1, 8):
    planeData.append([i, "A", "B", "C", "D"])


# Function to check if a seat is available
def takeSeat(row, seat):
    row = int(row)
    seatNum = 0
    # Converts the seat to an index for the 2nd list
    match seat:
        case "A":
            seatNum = 1
        case "B":
            seatNum = 2
        case "C":
            seatNum = 3
        case "D":
            seatNum = 4
    # Checks if seat is taken
    if planeData[row][seatNum] == "X":
        print("This seat is taken")
        return False
    else:
        # Swaps seat to taken
        planeData[row][seatNum] = "X"
        return True


def searchSeat():
    choosing = True
    # Loops through asking for row until its valid
    while choosing:
        clear()
        planePrint()
        answer = input("What row would you like to choose? \n>")
        # Using a try except to check if it's an integer instead of manual comparison
        try:
            # Checks if row is valid
            row = int(answer)
            if 1 <= row <= 7:
                seat = ""
                # Loops through asking for seat until its valid
                while seat != "A" and seat != "B" and seat != "C" and seat != "D":
                    clear()
                    planePrint()
                    print(f"Current row: {row}")
                    seat = input("Which seat would you like \n>").upper()
                    if seat == "A" or seat == "B" or seat == "C" or seat == "D":
                        # Checks if the seat is taken and if so will ask the user what they want to do next
                        if not takeSeat(row, seat):
                            check = ""
                            while check != "r" and check != "s" and check != "e":
                                check = input("Would you like to choose another [r]ow or [s]eat, or [e]xit? \n>").lower()
                                if check == "r":
                                    # Changes nothing so the loop goes back to asking for another seat
                                    print("")
                                elif check == "s":
                                    # Changes the seat to exit the loop and go back to choosing a new row
                                    seat = ""
                                elif check == "e":
                                    # Exits the row choosing loop
                                    choosing = False
                                else:
                                    print("Please enter a valid option")
                    # Seat not taken so it backs to main menu
                    else:
                        choosing = False
        except ValueError:
            print("Please enter a valid option")


# Print function for all the data because we lazy
def planePrint():
    for j in range(len(planeData)):
        print(f"{planeData[j][0]:^5}    {planeData[j][1]} {planeData[j][2]}    {planeData[j][3]} {planeData[j][4]}")


# Main menu function
def menu():
    print("Welcome")
    answer = True
    while answer:
        clear()
        planePrint()
        match input("What would you like to do \n1:Choose a seat\n2:Exit\n>"):
            case "1":
                searchSeat()
            case "2":
                answer = False
            case _:
                print("Please enter a valid option")


menu()
