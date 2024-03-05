from os import system, name
from time import sleep


def clear():
    system('cls' if name == 'nt' else 'clear')


# Using a loop to add all the data to the list because I am lazy
seatData = [
    [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
     "W", "X", "Y", "Z", "1", "2", "3", "4"]]
for i in range(1, 16):
    seatData.append([])
    seatData[i].append(i)
    for j in range(1, 31):
        seatData[i].append("#")

# Storage for purchases made
purchaseData = []
cPurchaseData = []

"""
Every time a ticket or group of tickets is purchased (meaning the user is prompted to enter the
seat(s) they wish to choose) the program should also be also displaying the total ticket prices
(see page 2 table for pricing) in addition to the current seating chart’s availability.
 Use a menu to allow your user to do more than just purchase tickets:
 1. Purchase Seat(s)
 2. View Total Ticket Sales
 3. View Sales Information
 4. Checkout
 5. Quit
o The program should keep a total of all ticket sales. The user should be given an option
of viewing this amount (menu 2).
o The program should also give the user an option to see a list of how many seats have
been sold, how many seats are available in each row, and how may seats are available
in the entire theater (menu 3).
o The program should allow the user to “check out” ie purchase their tickets. This option
should show the user how many tickets they’ve purchased, along with a summary of the
seats they’ve chosen, and the total cost for the tickets. Prompt the user for their amount,
display their change, and then reset the customer ticket counter – this means a new
customer could purchase more tickets without restarting the program, but the Total
Ticket Sales and the View Sales Information will stay unchanged.
The price for tickets are calculated using the following;
o Row 1 – Row 5 are $200.00
o Row 6 – Row 10 are $175.00
o Row 11 – Row 15 are $150.00
"""


def menu():
    operating = True
    while operating:
        clear()
        printSeats()
        match input("\t\t\t\t\t\tWelcome, please choose an option\n\t\t\t\t\t\t1: Purchase Seat(s)\n\t\t\t\t\t\t2: "
                    "View Total Ticket Sales\n\t\t\t\t\t\t3: View Sales Information\n\t\t\t\t\t\t4: "
                    "Checkout\n\t\t\t\t\t\t5: Quit\n>"):
            case "1":
                clear()
                purchaseSeats()
            case "2":
                clear()
                viewTotal()
            case "3":
                clear()
                viewInfo()
            case "4":
                clear()
                checkout()
            case "5":
                clear()
                operating = False
            case _:
                clear()
                print("Please enter a valid option")
                sleep(0.5)


def purchaseSeats():
    row = 0
    col = 0
    letCol = ""
    while row < 1:
        clear()
        printSeats()
        print("\t\t\t\t\t\tRows 1-5: $200.00\n\t\t\t\t\t\tRows 6-10 $175.00\n\t\t\t\t\t\tRows 11-15 $150.00")
        try:
            tempRow = int(input("\t\t\t\t\tPlease enter the row you wish to purchase a seat\n>"))
            if 1 <= tempRow <= 15:
                row = tempRow
            else:
                print("Please enter a valid option")
                sleep(0.5)
        except ValueError:
            print("Please enter a valid option")
            sleep(0.5)
    while col < 1:
        clear()
        printSeats()
        print(f"\t\t\t\t\t\tCurrent Row: {row}")
        tempCol = input("\t\t\t\t\tPlease enter the column you wish to purchase [A-Z then 1-4]\n>").upper()
        for i in range(1, len(seatData[0])):
            if tempCol == seatData[0][i]:
                col = i
                letCol = tempCol
                break
        else:
            print("Please enter a valid option")
            sleep(0.5)
    if seatData[row][col] == "#":
        seatData[row][col] = "*"
        cost = 0
        if row < 6:
            cost = 200
        elif row < 11:
            cost = 175
        else:
            cost = 150
        cPurchaseData.append([f"{row}{letCol}", cost])
        purchaseData.append([f"{row}{letCol}", cost])
        print(f"Seat {row}{letCol} will be ${cost}")
    else:
        print("That seat is taken")
        sleep(0.5)

    if input("Would you like to purchase another seat? (y/n)\n>").lower() == "y":
        purchaseSeats()


def printSeats():
    for row in seatData:
        print("\t\t", end="")
        for seat in range(len(row)):
            if seat != 8 and seat != 22:
                print(f"{row[seat]:^2}", end=" ")
            else:
                print(f"{row[seat]:^2}", end="     ")
        print("\n", end="")


def viewTotal():
    totalCost = 0
    print(f"{'Seat':4} | {'Cost':5}")
    for rec in purchaseData:
        totalCost += rec[1]
        print(f"{rec[0]:4} | ${rec[1]:4.2f}")
    print(f"Total Cost: ${totalCost:.2f}")
    input("Enter to go back to menu\n>")


def viewInfo():
    totalAvailable = 0
    totalSold = 0
    for i in range(1, len(seatData)):
        rowAvailable = 0
        for seat in seatData[i]:
            if seat == "*":
                totalSold += 1
            elif seat == "#":
                rowAvailable += 1
        print(f"Row {i:<2} has {rowAvailable:<2} seats available")
        totalAvailable += rowAvailable
    print(f"\nTotal Available Seats: {totalAvailable:<3}\nTotal Seats Sold: {totalSold:<3}")

    input("\nEnter to go back to menu\n>")


def checkout():
    totalCost = 0
    print(f"{'Seat':4} | {'Cost':5}")
    for rec in cPurchaseData:
        totalCost += rec[1]
        print(f"{rec[0]:4} | ${rec[1]:4.2f}")
    print(f"Total Cost: ${totalCost:.2f}")
    if input("Would you like to checkout?(y/n)\n>").lower() == "y":
        payment = 0
        while payment < totalCost:
            clear()
            print(f"Total Cost: ${totalCost:.2f}")
            print(f"Total Payment: ${payment:.2f}")
            try:
                payment = float(input("\t\t\t\t\tPlease enter the amount you wish to pay\n>"))
            except ValueError:
                print("Please enter a valid amount")
                sleep(0.5)
        change = payment - totalCost
        print(f"Total Payment: ${payment:.2f}")
        print(f"Change: ${change:.2f}")
        input("\nThank you for your purchase\nPress enter to go back to the menu")
        cPurchaseData.clear()


menu()
