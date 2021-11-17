from os import path
import login
from os.path import exists

def training_menu():
    path_to_file = "newtraining.txt"
    optionCounterList = []
    cmd = ""
    while (cmd != '0'):
        print("")
        print("**************")
        print("*  Training  *")
        print("**************")
        print("")
        print("Welcome to In College Training!")
        print("-----------------------------------------------------")
        print("| '1' to go to 'Training and Education'             |")
        print("| '2' to go to 'IT Help Desk'                       |")
        print("| '3' to go to 'Business Analysis and Strategy'     |")
        print("| '4' to go to 'Security'                           |")
        
        
        f = open("training.txt",'r')
        counter =  5
        for line in f:
            if line != '\n':
                line = line.rstrip()
                optionCounterList.append(counter)
                print("| '" + counter +"' to go to '" + line + "'             |")
        
        f.close()

        print("| '0' to return to main page                        |")
        print("-----------------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            TrainingAndEducation()
        elif (cmd == '2'):
            comingSoon()
        elif (cmd == '3'):
            BusinessAnalysis()
        elif (cmd == '4'):
            comingSoon()
        elif (cmd in optionCounterList):
            comingSoon()
        else:
            print("Invalid input, please try again")
            print("")

    return


def TrainingAndEducation():
    cmd = ""
    while cmd != '0':
        print("")
        print("**************************")
        print("* Training and Education *")
        print("**************************")
        print("")
        print("Welcome to Training and Education!")
        print("-----------------------------------------------------")
        print("| '1' to 'Train for an Interview'                   |")
        print("| '2' to 'Learn to Make the Perfect Resume'         |")
        print("| '3' to 'Sign Up for InCollege Classes'            |")
        print("| '4' to 'Test Your Skills'                         |")
        print("| '0' to return to main page                        |")
        print("-----------------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            underConstruction()
        elif (cmd == '2'):
            underConstruction()
        elif (cmd == '3'):
            underConstruction()
        elif (cmd == '4'):
            underConstruction()
        else:
            print("Invalid input, please try again")
            print("")

    return


def BusinessAnalysis():
    cmd = ""
    while cmd != '0':
        print("")
        print("*********************")
        print("* Business Analysis *")
        print("*********************")
        print("")
        print("-----------------------------------------------------------------")
        print("| '1' to learn How to use In College learning                   |")
        print("| '2' to learn Train the trainer                                |")
        print("| '3' to learn Gamification of learning                         |")
        print("| '0' to return to main page                                    |")
        print("|                                                               |")
        print("| Not seeing what you're looking for?                           |")
        print("| Sign in to see all 7,609 results!                             |")
        print("-----------------------------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            login.login("")
        elif (cmd == '2'):
            login.login("")
        elif (cmd == '3'):
            login.login("")
        else:
            print("Invalid input, please try again")
            print("")

    return


def underConstruction():
    cmd = ""
    while cmd != '0':
        cmd = input("Under Construction...press '0' to return to previous menu.")

def comingSoon():
    cmd = ""
    while cmd != '0':
        cmd = input("Coming Soon...press '0' to return to previous menu.")