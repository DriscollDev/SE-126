#Conor Driscoll, Lab 1, 1/10/2024


#Takes in 2 numbers and returns the difference between the 2
def difference(people, max_cap):
    return max_cap - people

#Checks if the user wants to continue
def decision(response):
    #Basic checks for if the user actually answered y or n
    if (response.lower() == "y"):
        return True
    elif (response.lower() =="n"):
        print("Goodbye")
        return False
    #if the user is blind or has fat fingers this recursive else will keep asking until they answer correctly
    else:
        print("Invalid Answer")
        answer = input("Do you want to continue?\n>")
        return decision(answer)

#Function to make errorhandling integer inputs easier
def roomget():
    #Loop to keep asking for max capacity until the user inputs an integer
    errorfree = False
    while(errorfree == False):
        try:
            maxp = int(input("What is the max capacity of the meeting room?\n>"))
            errorfree = True
        except:
            print("Input needs to be an integer")
    #Loop to keep asking for how many people are in the room until the user inputs an integer
    errorfree = False
    while(errorfree == False):
        try:
            people = int(input("How many people are in the meeting room?\n>"))
            errorfree = True
        except:
            print("Input needs to be an integer")
    return maxp,people

#Main (Function)
def main():
    #Willkommen
    print("Welcome to the Meeting Room Checker")
    #Main loop to keep getting more room checks
    cont = True
    while(cont):
        #Extra Variable to separate the 2 input integers
        roomst = roomget()
        #Runs the difference function and stores the output for use in the logic
        dif = difference(roomst[1], roomst[0])
        if(dif < 0):
            print(f"The max capacity is exceeded by {dif*-1}")
        elif(dif > 0):
            print(f"You are within the capacity with room for {dif} more people")
        else:
            print("You are at the capacity")
        #Final check to determine if the loop should keep running
        cont = decision(input("Do you want to continue? (y/n) \n>"))


    
#Main(Call)
main()