# Conor Driscoll Midterm
import csv
from os import system, name


def clear():
    system('cls' if name == 'nt' else 'clear')


class User:
    """
    This class represents a user in the casino.

    Attributes:
        id (int): The unique ID of the user.
        name (str): The username of the user.
        password (str): The password of the user.
        balance (int): The current balance of the user.
        winnings (int): The total winnings of the user.
        losses (int): The total losses of the user.
        purchases (int): The total balance purchased by the user.
    """

    def __init__(self, id, name, password, balance, winnings, losses, purchases):
        self.id = int(id)
        self.name = name
        self.password = password
        self.balance = int(balance)
        self.winnings = int(winnings)
        self.losses = int(losses)
        self.purchases = int(purchases)


def initializer():
    dictionary = {}
    # This function initializes the nameIdPairs dictionary by reading the data from the data.csv file.
    with open("data.csv") as csvfile:
        data = csv.reader(csvfile)
        for rec in data:
            # setting the key to the name and the value to the id
            dictionary[rec[1]] = rec[0]
    return dictionary


def dataFetcher(id):
    with open("data.csv") as csvfile:
        data = csv.reader(csvfile)
        for i in range(id):  # count from 0 to the ID
            next(data)  # and discard the rows
        return next(data)


# This function is used to log in to the casino.
def login():
    clear()
    ans = input("Enter your username \n>")
    # Returns the user object if the login is successful, else recursively calls the login function
    try:
        idL = nameIdPairs.get(ans.lower())
        userL = dataFetcher(int(idL))
        password = input("Enter your password \n>")
        if password == userL[2]:
            print(f"Welcome {ans}")
            return User(userL[0], userL[1], userL[2], userL[3], userL[4], userL[5], userL[6])
        else:
            return login()
    # Raises valueError if the username doesn't exist in database
    except ValueError:
        print("Invalid Username")
        return login()


def register(username):
    clear()
    if username == "":
        ans = input("Enter a username \n>").lower()
        if len(ans) < 3:
            print("Username must be at least 3 characters long")
            return register("")
        elif nameIdPairs.get(ans) is not None:
            print("Username already registered")
            return register("")
        else:
            return register(ans)
    else:
        ids = len(nameIdPairs)
        password = input("Enter your password \n>")
        confirm = input("Confirm your password \n>")
        if password == confirm:
            print(f"Welcome {username}, you get a complimentary $100 to start")
            userl = [ids, username, password, 100, 0, 0, 0]
            with open("data.csv", "a", newline="") as csvfile:
                # test = ["test", "test", "test", 0, 0, 0, 0]
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(userl)
            return User(userl[0], userl[1], userl[2], userl[3], userl[4], userl[5], userl[6])
        else:
            print("Passwords do not match")
            return register(username)


def startUp():
    print("\n=============================")
    print("Welcome to the Casino!")
    print("=============================\n")
    match input("Press 1 to Login, Press 2 to Register a new account, Press 3 to quit \n>"):
        case "1":
            clear()
            print(f"Welcome back")
            return login()
        case "2":
            clear()
            return register("")
        case "3":
            exit()
        case _:
            clear()
            print("Invalid Input")
            return startUp()


def main(casinoUser):
    print(f"You have ${casinoUser.balance} available")
    input("\n>")


nameIdPairs = initializer()
user = startUp()
main(user)
