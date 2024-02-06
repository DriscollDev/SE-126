#Conor Driscoll 2nd Midterm
import csv
from os import system, name
import random
from time import sleep

"""
Csv per adventure,
each row is new command
first value of each row should be an ID to allow linking
"""

def clear():
    system('cls' if name == 'nt' else 'clear')

class Character(object):
    name = ""
    clas = ""
    maxhp = 0
    pdef = 0
    mdef = 0
    hp = 0
    stats = {Str:0, Dex:0, Int:0}
    attacks = []

    def initialize(self, name,clas):
        self.name = name
        self.clas = clas
        match clas:
            case 'warrior':
                self.maxhp = 20
                self.hp = self.maxhp
                self.stats[Str] = 3
                self.stats[Dex] = 2
                self.stats[Int] = 1
                self.mdef = 1
                self.pdef = 4
                self.attacks.append(Attack("Sword",5,3,"physical","You slash the enemy with your sword"))
            case 'mage':
                self.maxhp = 10
                self.hp = self.maxhp
                self.stats[Str] = 1
                self.stats[Dex] = 2
                self.stats[Int] = 3
                self.mdef = 4
                self.pdef = 1
                self.attacks.append(Attack("Magic Bolt",5,5,"magic","You blast the enemy with you magic"))
            case 'rogue':
                self.maxhp = 15
                self.hp = self.maxhp
                self.stats[Str] = 1
                self.stats[Dex] = 3
                self.stats[Int] = 2
                self.mdef = 3
                self.pdef = 3
                self.attacks.append(Attack("Dagger",3,3,"physical","You stab the enemy with your dagger"))
                self.attacks.append(Attack("Enchanted Crossbow",3,3,"magic","You shoot the enemy with your hand crossbow"))

    def attack(self,attack,target):
        roll = random.randint(1,6)
        if(attack.type == "magic" and (roll + attack.bonus) > target.mdef):
            print(f"You hit {target.name} for {attack.damage} damage!")
            target.hp -= attack.damage
        elif((roll + attack.bonus) > target.pdef):
            print(f"You hit {target.name} for {attack.damage} damage!")
            target.hp -= attack.damage
        else:
            print(f"You miss :(")

class Attack(object):
    name = ""
    bonus = 0
    damage = 0
    type = ""
    description = ""
    def __init__(self,name,bonus,damage,type,description):
        self.name = name
        self.bonus = bonus
        self.damage = damage
        self.type = type
        self.description = description

class Monster(object):
    name = ""
    hp = 0
    pdef = 0
    mdef = 0
    attacks = []

def textBlock(commandList):
    #Prints out information and shows player options for their next move
    return None

def combat(commandList):
    #Plays a combat sequence
    return None

def skillCheck(commandList):
    #Shows a skill check
    return None

def characterMaker():
    #Creates a new character
    clear()
    print("Welcome adventurer, tell me what is your name?")
    name = input(">")
    clear()
    clasChoice = ""
    print("What class would you like to be?")
    print("Warrior, Has the most health of the classes, good defence against physical attacks,and low damage")
    print("Mage, Has the least health, good magic defence, and high damage")
    print("Rogue, Has the middle amount of health, defence, and damage")
    clasChoice = input(">").lower()
    while (clasChoice != "warrior" and clasChoice != "mage" and clasChoice != "rogue"):
        clear()
        print("Please enter a valid class")
        print("----------------------------------------------------------------")
        print("What class would you like to be?")
        print("Warrior, Has the most health of the classes, good defence against physical attacks,and low damage")
        print("Mage, Has the least health, good magic defence, and high damage")
        print("Rogue, Has the middle amount of health, defence, and damage")
        clasChoice = input(">").lower()
    clear()
    return Character(name,clas)