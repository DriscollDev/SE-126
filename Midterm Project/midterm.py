# Conor Driscoll Midterm
import csv
from os import system, name
import random


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


def record(casinoUser):
    userl = [casinoUser.id, casinoUser.name, casinoUser.password, casinoUser.balance, casinoUser.winnings,
             casinoUser.losses, casinoUser.purchases]
    data2 = []
    with open("data.csv", "r", newline="") as csvfile:
        data = csv.reader(csvfile)
        for rec in data:
            data2.append(rec)
        data2[casinoUser.id] = userl
    with open("data.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data2)


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


def accountInfo(casinoUser):
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
            money = input("How much would you like to purchase \n>")
            casinoUser.balance += int(money)
            casinoUser.purchases += int(money)
            return casinoUser
        case "2":
            return casinoUser


def deathscrown(casinoUser):
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
        bet = int(input("Input your bet: "))
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            print(f"You have bet ${bet}")
            print("--------------------------------------------------------")
            place = int(
                input(
                    "What face would you like to bet on? \n 1:Crown \n 2:Skull \n 3:Earth \n 4:Fire \n 5:Water \n "
                    "6:Air \n 7:Exit\n:"
                ))
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
                    if input("Would you like to play again? (y/n):") == "y":
                        return deathscrown(casinoUser)
                    else:
                        return casinoUser
                else:
                    print("You lost!")
                    casinoUser.balance -= bet
                    casinoUser.losses += bet
                    print(f"Your current balance is ${casinoUser.balance}")
                    if input("Would you like to play again? (y/n):") == "y":
                        return deathscrown(casinoUser)
                    else:
                        return casinoUser
    else:
        return casinoUser


def blackjack(casinoUser):
    print("\n=============================\n")
    print(
        "Welcome to Dice Blackjack \n The rules are simple, you are trying to get the closest to 21 you can without "
        "going over. You start off with 2 dice of 1-10. \n Each turn you can choose to roll another or stand. \n Also "
        "if you have a 1 rolled that can be substituted as an 11 depending on what you have. \n Good Luck! \n"
    )
    if input("Do you wish to play?(y/n)") == "y":
        print("How much would you like to bet?")
        bet = int(input("Input your bet: "))
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
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
                    if input("Would you like to play again? (y/n):") == "y":
                        return blackjack(casinoUser)
                    else:
                        return casinoUser
                else:
                    print("Blackjack!")
                    casinoUser.balance += (bet * 1.5)
                    casinoUser.winnings += (bet * 1.5)
                    print(f"Your current balance is ${casinoUser.balance}")
                    if input("Would you like to play again? (y/n):") == "y":
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
                    print("You busted!")
                    casinoUser.balance -= bet
                    casinoUser.losses += bet
                    print(f"Your current balance is ${casinoUser.balance}")
                    if input("Would you like to play again? (y/n):") == "y":
                        blackjack(casinoUser)
                    return casinoUser

                print("--------------------------------------------------------")
                print(f"Dealer Cards: {dealer_cards[0]}")
                print(f"Player Cards: {player_cards} \nPlayer Total: {player_total}")
                print("--------------------------------------------------------")
                print("What would you like to do? \n 1:Roll \n 2:Stand")
                choice = int(input("Input your choice: "))
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
    if input("Would you like to play again? (y/n):") == "y":
        return blackjack(casinoUser)
    return casinoUser


def dice712(casinoUser):
    print("\n=============================\n")
    print(
        "Welcome 7-12 Dice, rules are really simple. You buy in for 50$ and roll 2 dice, if the dice add up to 7 or "
        "12 you win. If you want to you can double down your bet to add another die."
    )
    if input("Ready to play? (y/n): ") == "y":
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
            if input("Would you like to play again? (y/n): ") == "y":
                return dice712(casinoUser)
            else:
                return casinoUser
        else:
            if (input("Would you like to double down to roll another die? (y/n)\n: ")
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
                if input("Would you like to play again? (y/n): ") == "y":
                    return dice712(casinoUser)
                else:
                    return casinoUser
            else:
                print("You lost!")
                casinoUser.balance -= 50
                casinoUser.losses += 50
                print(f"Your current balance is ${casinoUser.balance}")
                if input("Would you like to play again? (y/n): ") == "y":
                    return dice712(casinoUser)
                else:
                    return casinoUser
    return casinoUser


def basicroulette(casinoUser):
    type = "none"
    bet = 0
    number = 0
    choice = "none"
    print("\n=============================\n")
    print(
        "Welcome to Roulette. The rules are simple, a number between 0 and 36 will be chosen at randomly.\nYou can "
        "bet on these categories \n1:Specific number between 0-36 \n2:Even or odd \n3:Red or black \n4:12 number ranges"
    )
    answer = int(input("Which type of bet would you like to do?: "))
    print("----------------------------------------------------------")
    if answer == 1:
        type = "Number"
        print("You have chosen to bet on a specific number.")
        bet = int(input("How much would you like to bet?: "))
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            print(f"You have bet ${bet}")
            number = int(input("What number would you like to bet on?: "))
            if number > 36 or number < 0:
                print("That number is not between 0 and 36")
    elif answer == 2:
        type = "E/O"
        print("You have chosen to bet on even or odd.")
        bet = int(input("How much would you like to bet?: "))
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            print(f"You have bet ${bet}")
            choice = int(
                input(
                    "Would you like to bet on even or odd?: \n 1:Even \n 2:Odd \n: ")
            )
            if choice == 1:
                choice = "even"
            elif choice == 2:
                choice = "odd"
            else:
                print("That is not a valid choice.")
    elif answer == 3:
        type = "R/B"
        print("You have chosen to bet on red or black.")
        bet = int(input("How much would you like to bet?: "))
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            print(f"You have bet ${bet}")
            choice = int(
                input(
                    "Would you like to bet on red or black?: \n 1:Red \n 2:Black \n: "
                ))
            if choice == 1:
                choice = "red"
            elif choice == 2:
                choice = "black"
            else:
                print("That is not a valid choice.")
    elif answer == 4:
        type = "Range"
        print("You have chosen to bet on 12 number ranges.")
        bet = int(input("How much would you like to bet?: "))
        if bet > casinoUser.balance:
            print("You don't have enough money to bet that much.")
        else:
            print(f"You have bet ${bet}")
            choice = int(
                input(
                    "Would you like to bet on ranges of numbers?: \n 1:1-12 \n 2:13-24 \n 3:25-36"
                ))
            if choice == 1:
                choice = "R1"
            elif choice == 2:
                choice = "R2"
            elif choice == 3:
                choice = "R3"
            else:
                print("That is not a valid choice.")
    else:
        print("That is not a valid choice.")
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

    if input("Would you like to play again? (y/n): ") == "y":
        return basicroulette(casinoUser)

    return casinoUser


def main(casinoUser):
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
                        clear()
                        casinoUser = deathscrown(casinoUser)
                    case "2":
                        clear()
                        casinoUser = blackjack(casinoUser)
                    case "3":
                        clear()
                        casinoUser = dice712(casinoUser)
                    case "4":
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
