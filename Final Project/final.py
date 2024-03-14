import csv
from os import system, name
from time import sleep


# This program will emulate a virtual library program where you can view data on books by searching for them or just
# sorting them and viewing them

def clear():
    system('cls' if name == 'nt' else 'clear')


# Initializing the list for the books to be stored in
library = []
cart = []
checkedOut = []


# Title,Author,Genre,SubGenre,Height,Publisher

# The object that all the csv data will be stored in
class Book:
    searchTitle = ""
    displayTitle = ""
    authorF = ""
    authorL = ""
    publisher = ""
    genre = ""
    subGenre = ""

    # Changed the default print method for the object mainly for testing
    def __str__(self):
        return f"Title: {self.displayTitle}, First Name: {self.authorF}, Last Name: {self.authorL}, Genre: {self.genre}, SubGenre: {self.subGenre}"

    # Initializer, the title and author take a bit more processing so that's stored later
    def __init__(self, publisher, genre, subGenre):
        self.publisher = publisher
        self.genre = genre
        self.subGenre = subGenre


# File reader and data populator
with open("books.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # starts off by just adding the easy-to-read properties
        newBook = Book(row[5].strip(), row[2].strip(), row[3].strip())
        try:
            # Attempts to split and assign values to first and last name, if the author only has one it will break
            # and assign it to the last
            author = row[1].strip().split(',')
            newBook.authorF = author[1].strip()
            newBook.authorL = author[0].strip()
        except:
            newBook.authorL = row[1]
        try:
            # Same split attempt for the title, as some books with "the" or "a" at the start of the title shouldn't be
            # searched by that
            title = row[0].strip().split(',')
            newBook.searchTitle = title[0].strip()
            newBook.displayTitle = f"{title[1].strip()} {title[0].strip()}"
        except:
            # if the title is regular it will assign standardly
            newBook.displayTitle = row[0].strip()
            newBook.searchTitle = row[0].strip()
        # adds the finalized book to the list
        library.append(newBook)


# Basic bubblesort modified to add in a specific tag to sort by
def bubbleSort(unSortList, tag):
    for i in range(len(unSortList) - 1):
        for j in range(len(unSortList) - i - 1):
            # Where the tag is checked to sort by (genre, title, author name)
            if getattr(unSortList[j], tag) > getattr(unSortList[j + 1], tag):
                # One line swap
                unSortList[j], unSortList[j + 1] = unSortList[j + 1], unSortList[j]
    return unSortList


# Basic search that gets multiple results
def seqSearch(query, tag, list):
    hitList = []
    for rec in list:
        if getattr(rec, tag).lower() == query.lower():
            hitList.append(rec)
    return hitList


# Print function because I didn't want to copy and paste it more than once
def printLibrary(tempLibrary):
    print(f"{'Book Title':^55}\t{'Author Name':^20}\t{'Genre':^10}\t{'Sub Genre':^10}")
    for i in range(len(tempLibrary)):
        print(f"{i+1}: {tempLibrary[i].displayTitle:55}\t{tempLibrary[i].authorF:10} {tempLibrary[i].authorL:10}\t{tempLibrary[i].genre:10}\t{tempLibrary[i].subGenre:10}")


# Menu for searching for specific book, author,genre
def searchBooks():
    choice = ""
    while choice != "4":
        clear()
        print(
            "What category do you want to sort by?\n1:Author Last Name\n2:Title\n3:Genre\n4:Go Back "
            "to Main Menu")
        choice = input(">")
        match choice:
            case "1":
                name = input("Enter the Author's Last Name \n>")
                tempLibrary = seqSearch(name, "authorL", library)
                printLibrary(tempLibrary)
                addCart(tempLibrary)
            case "2":
                title = input("Enter the Book Title \n>")
                tempLibrary = seqSearch(title, "searchTitle", library)
                printLibrary(tempLibrary)
                addCart(tempLibrary)
            case "3":
                genre = input("Enter the Genre \n>")
                tempLibrary = seqSearch(genre, "genre", library)
                printLibrary(tempLibrary)
                addCart(tempLibrary)
            case "4":
                sleep(0.5)
            case _:
                print("Please enter a valid option")
                sleep(0.5)


def addCart(tempLibrary):
    trapped = True
    answer = 0
    while trapped:
        try:
            answer = int(input("Enter 0 to go back to menu, or enter a number to add a book to your cart\n>"))
            trapped = False
        except ValueError:
            print("Please enter a valid option")
            sleep(0.5)
    if answer != 0:
        bookGrab = tempLibrary.pop(answer - 1)
        cart.append(bookGrab)
        library.remove(bookGrab)


def checkout():
    print("Cart")
    printLibrary(cart)
    trap = True
    while trap:
        match input("Do you want to check out these books (y/n)\n>").lower():
            case "y":
                for book in cart:
                    checkedOut.append(book)
                cart.clear()
                trap = False
            case "n":
                sleep(0.5)
                trap = False
            case _:
                print("Please enter a valid option")
                sleep(0.5)


# Menu for sorting by title, author, genre
def listBooks():
    choice = ""
    while choice != "4":
        clear()
        print(
            "What category do you want to sort by?\n1:Author Last Name\n2:Title\n3:Genre\n4:Go Back "
            "to Main Menu")
        choice = input(">")
        match choice:
            case "1":
                tempLibrary = bubbleSort(library, "authorL")
                printLibrary(tempLibrary)
                input(">")

            case "2":
                tempLibrary = bubbleSort(library, "searchTitle")
                printLibrary(tempLibrary)
                input(">")
            case "3":
                tempLibrary = bubbleSort(library, "genre")
                printLibrary(tempLibrary)
                input(">")
            case "4":
                sleep(0.5)
            case _:
                print("Please enter a valid option")
                sleep(0.5)


# Main menu
def main():
    choice = ""
    while choice != "5":
        clear()
        print("Welcome to the library!\nWhat would you like to do?\n1: Search for and check out books\n2: View all "
              "books\n3: Checkout\n4: View Checked Out Books\n5: Exit")
        choice = input("Enter your choice\n>")
        match choice:
            case "1":
                searchBooks()
            case "2":
                listBooks()
            case "3":
                checkout()
            case "4":
                printLibrary(checkedOut)
                input(">")
            case "5":
                print("Thank you for using the library!")
                sleep(0.5)
            case _:
                print("Please enter a valid option")
                sleep(0.5)


main()
