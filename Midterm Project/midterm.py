# Conor Driscoll Midterm
import csv
from os import system, name
import random
from time import sleep

filepath = "data.csv"
"""
This script is a casino game.

Functions
- startUp: This function initializes the game and displays the main menu.
- login: This function is used to log in to the casino.
- register: This function is used to register a new account.
- record: This function is used to record the changes made to the user's account.
- accountInfo: This function is used to display the user's account information.
- deathscrown: This function is used to play Deaths Crown.
- blackjack: This function is used to play Blackjack.
- dice712: This function is used to play Dice 7-12.
- basicroulette: This function is used to play basic roulette.
- main: This function is the main function of the game, which controls the flow of the game.

Classes
- User: This class represents a user in the casino.

Global Variables
- nameIdPairs: This variable is a dictionary that maps usernames to user IDs.
"""


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
    with open(filepath) as csvfile:
        data = csv.reader(csvfile)
        for rec in data:
            # setting the key to the name and the value to the id
            dictionary[rec[1]] = rec[0]
    return dictionary


def dataFetcher(id):
    with open(filepath) as csvfile:
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
    """
    This function registers a new user with the casino.
    with a recursive setup to allow for only asking 1 value at a time, and instead of asking for a new username if the password is invalid it should just ask for another password
    """
    # If the username is blank or empty, ask for a username
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
    # otherwise just ask for a password
    else:
        ids = len(nameIdPairs)
        password = input("Enter your password \n>")
        confirm = input("Confirm your password \n>")
        if password == confirm:
            print(f"Welcome {username}, you get a complimentary $100 to start")
            userl = [ids, username, password, 100, 0, 0, 0]
            with open(filepath, "a", newline="") as csvfile:
                # test = ["test", "test", "test", 0, 0, 0, 0]
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(userl)
            return User(userl[0], userl[1], userl[2], userl[3], userl[4], userl[5], userl[6])
        else:
            print("Passwords do not match")
            return register(username)


def record(casinoUser):
    # Updates the csv with current user values

    # Turns the user object back into a list
    userl = [casinoUser.id, casinoUser.name, casinoUser.password, casinoUser.balance, casinoUser.winnings,
             casinoUser.losses, casinoUser.purchases]
    # Empty list to temporarily hold the data from the csv
    data2 = []
    with open(filepath, "r", newline="") as csvfile:
        data = csv.reader(csvfile)
        for rec in data:
            data2.append(rec)
        # Overwrites the user's data with the new values
        data2[casinoUser.id] = userl
    with open(filepath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data2)


def startUp():
    # All this is doing is displaying a 1 time menu for logging in, registering or just quitting immediately
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


def accountInfo(casinoUser):
    """
    This function displays the user's account information.
    And allows for purchasing of more balance
    """
    clear()
    print("\n=============================")
    print(f"Name: {casinoUser.name}")
    print(f"Balance: ${casinoUser.balance}")
    print(f"Winnings: ${casinoUser.winnings}")
    print(f"Losses: ${casinoUser.losses}")
    print(f"Purchases: ${casinoUser.purchases}")
    print("================================")
    print("What would you like to do")
    match input("1: Purchase more balance\n2: Back to menu\n>"):
        case "1":
            clear()
            money = validate("int", "How much would you like to purchase \n>")
            casinoUser.balance += int(money)
            casinoUser.purchases += int(money)
            return casinoUser
        case "2":
            return casinoUser
        case _:
            clear()
            print("Invalid Input")
            return accountInfo(casinoUser)


def validate(type, string, expected=None):
    if expected is None:
        expected = []
    match type:
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


def deathscrown(casinoUser):
    """
    This function allows the user to play the game of Deaths Crown
    The game is played by betting on 1 of 6 values then rolling 3 6 sided dice, winning money equal to the bet for each dice that lands on the value betted on
    """
    if casinoUser.balance <= 0:
        print("You don't have enough balance")
        return casinoUser
    print("\n==========================================================\n")
    print(
        "Welcome to Deaths Crown \n The Rules are simple we will roll 3 special 6 sided dice, with the faces being\n "
        "Crown\n Skull\n Earth\n Fire\n Water\n Air \nYou just have to bet on one of the possible results and you can "
        "win back money based on the number of dice that match. \n Good Luck!"
    )
    # print(answer)
    if input("Ready to play?(y/n): ") == "y":
        print()
        print("How much would you like to bet?")
        bet = validate("int", "Input your bet: ")
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            print(f"You have bet ${bet}")
            print("--------------------------------------------------------")
            place = int(
                validate("list", "What face would you like to bet on? \n 1:Crown \n 2:Skull \n 3:Earth \n 4:Fire "
                                 "\n 5:Water \n 6:Air \n 7:Exit\n>", ["1", "2", "3", "4", "5", "6", "7"]))
            if place == 7:
                print("Thanks for playing!")
                return casinoUser
            else:
                wins = 0
                for i in range(3):
                    dice = random.randint(1, 6)
                    # print(dice)
                    if dice == place:
                        wins += 1
                    match dice:
                        case 1:
                            print("Crown")
                        case 2:
                            print("Skull")
                        case 3:
                            print("Earth")
                        case 4:
                            print("Fire")
                        case 5:
                            print("Water")
                        case 6:
                            print("Air")
                if wins > 0:
                    print("----------------------------------------------------------")
                    profit = bet * wins
                    print(f"You win ${profit}!")
                    casinoUser.balance += profit
                    casinoUser.winnings += profit
                    print(f"Your current balance is ${casinoUser}")
                    if input("Would you like to play again? (y/n):").lower() == "y":
                        return deathscrown(casinoUser)
                    else:
                        return casinoUser
                else:
                    print("You lost!")
                    casinoUser.balance -= bet
                    casinoUser.losses += bet
                    print(f"Your current balance is ${casinoUser.balance}")
                    if input("Would you like to play again? (y/n):").lower() == "y":
                        return deathscrown(casinoUser)
                    else:
                        return casinoUser
    else:
        return casinoUser


def blackjack(casinoUser):
    """
    This function allows the user to play the game of Dice Blackjack
    The game is played by getting 2 10 sided dice and rolling them to gain the value of your hand, competing against the dealer. The player then gains the option to roll another dice (hitting) but if the player goes over 21 then they lose. Rolling 1 on the dice will be simultaneously be worth both 1 and 11, allowing the player to roll more if they want
    """
    if casinoUser.balance <= 0:
        print("You don't have enough balance")
        return casinoUser
    print("\n=============================\n")
    print(
        "Welcome to Dice Blackjack \n The rules are simple, you are trying to get the closest to 21 you can without "
        "going over. You start off with 2 dice of 1-10. \n Each turn you can choose to roll another or stand. \n Also "
        "if you have a 1 rolled that can be substituted as an 11 depending on what you have. \n Good Luck! \n"
    )
    if input("Do you wish to play?(y/n)") == "y":
        print("How much would you like to bet?")
        bet = validate("int", "Input your bet: ")
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            clear()
            print(f"You have bet ${bet}")
            print("--------------------------------------------------------")
            dealer_cards = [random.randint(1, 10), random.randint(1, 10)]
            player_cards = [random.randint(1, 10), random.randint(1, 10)]
            player_total = 0
            playerace = False
            gambling = True
            if ((player_cards[0] == 1 or player_cards[1] == 1)
                    and (player_cards[0] == 10 or player_cards[1] == 10)):
                if ((dealer_cards[0] == 1 or dealer_cards[1] == 1)
                        and (dealer_cards[0] == 10 or dealer_cards[1] == 10)):
                    print("Both players have Blackjack, you tie!")
                    print(f"Your current balance is ${casinoUser}")
                    if input("Would you like to play again? (y/n):").lower() == "y":
                        return blackjack(casinoUser)
                    else:
                        return casinoUser
                else:
                    print("Blackjack!")
                    casinoUser.balance += (bet * 1.5)
                    casinoUser.winnings += (bet * 1.5)
                    print(f"Your current balance is ${casinoUser.balance}")
                    if input("Would you like to play again? (y/n):").lower == "y":
                        return blackjack(casinoUser)
                    else:
                        return casinoUser

            while gambling:
                for i in range(len(player_cards)):
                    if player_cards[i] == 1:
                        playerace = True
                if playerace:
                    player_total = (sum(player_cards) + 10)
                    if player_total > 21:
                        player_total -= 10
                else:
                    player_total = sum(player_cards)

                if player_total > 21:
                    print(f"Player Cards: {player_cards} \nPlayer Total: {player_total}")
                    print("You busted!")
                    casinoUser.balance -= bet
                    casinoUser.losses += bet
                    print(f"Your current balance is ${casinoUser.balance}")
                    if input("Would you like to play again? (y/n):").lower() == "y":
                        blackjack(casinoUser)
                    return casinoUser
                clear()
                print("--------------------------------------------------------")
                print(f"Dealer Cards: {dealer_cards[0]}")
                print(f"Player Cards: {player_cards} \nPlayer Total: {player_total}")
                print("--------------------------------------------------------")
                print("What would you like to do? \n 1:Roll \n 2:Stand")
                choice = int(validate("list", "Input your choice: ", ["1", "2"]))
                if choice == 1:
                    player_cards.append(random.randint(1, 10))
                else:
                    gambling = False

            dealerace = False
            for i in range(len(dealer_cards)):
                if dealer_cards[i] == 1:
                    dealerace = True
            if dealerace:
                dealertotal = (sum(dealer_cards) + 10)
                if dealertotal > 21:
                    dealertotal -= 10
            else:
                dealertotal = sum(dealer_cards)

            dealertotal = sum(dealer_cards)

            while dealertotal < 17:
                clear()
                print(f"Dealer Cards: {dealer_cards}")
                print(f"Dealer Total: {dealertotal}")
                print("Hitting...")
                dealer_cards.append(random.randint(1, 10))
                dealertotal = sum(dealer_cards)
                for i in range(len(dealer_cards)):
                    if dealer_cards[i] == 1:
                        dealerace = True
                if dealerace:
                    dealertotal = (sum(dealer_cards) + 10)
                    if dealertotal > 21:
                        dealertotal -= 10
                else:
                    dealertotal = sum(dealer_cards)

                dealertotal = sum(dealer_cards)
                sleep(1)
            clear()
            print(f"User Hand is {player_cards} and total is {player_total}")
            print(f"Dealer Hand is {dealer_cards} and total is {dealertotal}")
            if player_total > dealertotal:
                print("You won!")
                casinoUser.balance += bet
                casinoUser.winnings += bet
            elif dealertotal > player_total:
                print("You lost!")
                casinoUser.balance -= bet
                casinoUser.losses += bet
            else:
                print("You tied!")

    print(f"Your current balance is ${casinoUser.balance}")
    if input("Would you like to play again? (y/n):").lower() == "y":
        return blackjack(casinoUser)
    return casinoUser


def dice712(casinoUser):
    """
    This function allows the user to play the game of Dice 7-12
    The game is player by rolling 2 6 sided dice, if they add to 7 or 12 they win. But if they dont the player can double down to roll 1 more die
    """
    if casinoUser.balance <= 0:
        print("You don't have enough balance")
        return casinoUser
    print("\n=============================\n")
    print(
        "Welcome 7-12 Dice, rules are really simple. You buy in for 50$ and roll 2 dice, if the dice add up to 7 or "
        "12 you win. If you want to you can double down your bet to add another die."
    )
    if input("Ready to play? (y/n): ").lower() == "y":
        if casinoUser.balance < 50:
            print("You don't have enough money to play.")
            return casinoUser
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum = dice1 + dice2
        print(f"You rolled {dice1} and {dice2}. Which add to {sum}")
        if sum == 7 or sum == 12:
            print("You win!")
            casinoUser.balance += 50
            casinoUser.winnings += 50
            print(f"Your current balance is ${casinoUser}")
            if input("Would you like to play again? (y/n): ").lower() == "y":
                return dice712(casinoUser)
            else:
                return casinoUser
        else:
            if (input("Would you like to double down to roll another die? (y/n)\n: ").lower()
                    == "y"):
                if casinoUser.balance < 100:
                    print("You do not have enough money to double down.")
                    return casinoUser
                dice3 = random.randint(1, 6)
                sum2 = sum + dice3
                print(f"You rolled {dice3}. Which add to {sum2}")
                if sum2 == 7 or sum2 == 12:
                    print("You win!")
                    casinoUser.balance += 100
                    casinoUser.winnings += 100
                else:
                    print("You lost!")
                    casinoUser -= 100
                    casinoUser.losses += 100
                print(f"Your current balance is ${casinoUser.balance}")
                if input("Would you like to play again? (y/n): ").lower() == "y":
                    return dice712(casinoUser)
                else:
                    return casinoUser
            else:
                print("You lost!")
                casinoUser.balance -= 50
                casinoUser.losses += 50
                print(f"Your current balance is ${casinoUser.balance}")
                if input("Would you like to play again? (y/n): ").lower() == "y":
                    return dice712(casinoUser)
                else:
                    return casinoUser
    return casinoUser


def basicroulette(casinoUser):
    if casinoUser.balance <= 0:
        print("You don't have enough balance")
        return casinoUser
    # Roulette, you play by betting on a value, a color, even/odd, or number ranges. If the randomly chosen value
    # matches the description of the bet the player wins
    type = "none"
    bet = 0
    number = 0
    choice = "none"
    print("\n=============================\n")
    print(
        "Welcome to Roulette. The rules are simple, a number between 0 and 36 will be chosen at randomly.\nYou can "
        "bet on these categories \n1:Specific number between 0-36 \n2:Even or odd \n3:Red or black \n4:12 number ranges"
    )
    print("----------------------------------------------------------")

    match validate("list", "Which type of bet would you like to do?: ", ["1", "2", "3", "4"]):
        case '1':
            type = "Number"
            print("You have chosen to bet on a specific number.")
            bet = validate("int", "Input your bet: ")
            if bet > casinoUser.balance:
                print("You don't have enough money to bet that much.")
            else:
                print(f"You have bet ${bet}")
                number = validate("int", "What number would you like to bet on?: ")
                if number > 36 or number < 0:
                    print("That number is not between 0 and 36")
        case '2':
            type = "E/O"
            print("You have chosen to bet on even or odd.")
            bet = validate("int", "Input your bet: ")
            if bet > casinoUser.balance:
                print("You don't have enough money to bet that much.")
            else:
                print(f"You have bet ${bet}")
                choice = validate("list", "Would you like to bet on even or odd?: \n 1:Even \n 2:Odd \n: ", ["1", "2"])
                if choice == "1":
                    choice = "even"
                elif choice == "2":
                    choice = "odd"
        case '3':
            type = "R/B"
            print("You have chosen to bet on red or black.")
            bet = validate("int", "Input your bet: ")
            if bet > casinoUser.balance:
                print("You don't have enough money to bet that much.")
            else:
                print(f"You have bet ${bet}")
                choice = validate("list","Would you like to bet on red or black?: \n 1:Red \n 2:Black \n: ",["1","2"])
                if choice == 1:
                    choice = "red"
                elif choice == 2:
                    choice = "black"
        case '4':
            type = "Range"
            print("You have chosen to bet on 12 number ranges.")
            bet = validate("int", "Input your bet: ")
            if bet > casinoUser.balance:
                print("You don't have enough money to bet that much.")
            else:
                print(f"You have bet ${bet}")
                choice = validate("list","Would you like to bet on ranges of numbers?: \n 1:1-12 \n 2:13-24 \n 3:25-36",["1","2","3"])
                if choice == 1:
                    choice = "R1"
                elif choice == 2:
                    choice = "R2"
                elif choice == 3:
                    choice = "R3"
    print("----------------------------------------------------------")
    print("Spinning the wheel...")
    roll = random.randint(0, 36)
    print(f"The wheel landed on {roll}")
    if type == "Number":
        if roll == number:
            profit = bet * 35
            print(f"You won ${profit}!")
            casinoUser.balance += profit
            casinoUser.winnings += profit
            print(f"You now have ${casinoUser.balance} dollars.")
        else:
            print("You lost!")
            casinoUser.balance -= bet
            casinoUser.losses += bet
    elif type == "E/O":
        if roll % 2 == 0 and choice == "even":
            print(f"You won ${bet}!")
            casinoUser.balance += bet
            casinoUser.winnings += bet
            print(f"You now have ${casinoUser.balance} dollars.")
        elif (roll % 2 == 1) and choice == "odd":
            print(f"You won ${bet}!")
            casinoUser.balance += bet
            casinoUser.winnings += bet
            print(f"You now have ${casinoUser.balance} dollars.")
        else:
            print("You lost!")
            casinoUser.balance -= bet
            casinoUser.losses += bet
            print(f"You now have ${casinoUser.balance} dollars.")
    elif type == "R/B":
        rollcolor = "none"
        reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        blacks = [
            2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
        ]
        for i in range(18):
            if roll == reds[i]:
                rollcolor = "red"
            elif roll == blacks[i]:
                rollcolor = "black"

        if choice == rollcolor:
            print(f"You won ${bet}!")
            casinoUser.balance += bet
            casinoUser.winnings += bet
            print(f"You now have ${casinoUser.balance} dollars.")
        else:
            print("You lost!")
            casinoUser.balance -= bet
            casinoUser.losses += bet
            print(f"You now have ${casinoUser.balance} dollars.")
    elif type == "Range":
        if 1 <= roll <= 12 and choice == "R1":
            print(f"You won ${bet}!")
            casinoUser.balance += bet
            casinoUser.winnings += bet
            print(f"You now have ${casinoUser.balance} dollars.")
        elif 13 <= roll <= 24 and choice == "R2":
            print(f"You won ${bet}!")
            casinoUser.balance += bet
            casinoUser.winnings += bet
            print(f"You now have ${casinoUser.balance} dollars.")
        elif 25 <= roll <= 36 and choice == "R3":
            print(f"You won ${bet}!")
            casinoUser.balance += bet
            casinoUser.winnings += bet
            print(f"You now have ${casinoUser.balance} dollars.")
        else:
            print("You lost!")
            casinoUser.balance -= bet
            casinoUser.losses += bet
            print(f"You now have ${casinoUser.balance} dollars.")

    if input("Would you like to play again? (y/n): ").lower() == "y":
        return basicroulette(casinoUser)

    return casinoUser


def main(casinoUser):
    # Main menu
    gaming = "y"
    while gaming.lower() == "y":
        clear()
        print(f"You have ${casinoUser.balance} available")
        match input(f"What would you like to do?\n1. Play a game\n2. View account info\n3. Exit\n>"):
            case "1":
                clear()
                print("Which Game would you like to play?")
                print("1: Deaths Crown \n2: Blackjack \n3: Dice 7-12 \n4: Roulette \n5: Back to menu")
                match input(">"):
                    case "1":
                        if casinoUser.balance == 0:
                            print("You do not have enough money!")
                            clear()
                        else:
                            clear()
                            casinoUser = deathscrown(casinoUser)
                    case "2":
                        if casinoUser.balance == 0:
                            print("You do not have enough money!")
                        else:
                            clear()
                            casinoUser = blackjack(casinoUser)
                    case "3":
                        if casinoUser.balance == 0:
                            print("You do not have enough money!")
                        else:
                            clear()
                            casinoUser = dice712(casinoUser)
                    case "4":
                        if casinoUser.balance == 0:
                            print("You do not have enough money!")
                        else:
                            clear()
                            casinoUser = basicroulette(casinoUser)
            case "2":
                clear()
                casinoUser = accountInfo(casinoUser)
            case "3":
                clear()
                print("That you for playing!")
                record(casinoUser)
                gaming = "n"
            case _:
                input("That is not a valid choice.\n>")


nameIdPairs = initializer()
main(startUp())
