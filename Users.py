import random

import usefulLinks
from views import mainPage
from validatePass import validatePass
import login
import importantLinks
import training
from itertools import groupby

class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True

def output_jobs():
    aFile = open("jobs.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    wFile = open("MyCollege_jobs.txt", "w")    
    for line in lines:
        if line != '\n':
            wFile.write(line)
            wFile.write("=====" + '\n')
    wFile.close()


def output_userProfiles():
    aFile = open("profile.txt", "r")
    linea = aFile.readlines()
    aFile.close()

    bFile = open("profile_education.txt", "r")
    lineb = bFile.readlines()
    bFile.close()

    cFile = open("profile_experience.txt", "r")
    linec = cFile.readlines()
    cFile.close()

    wFile = open("profiletempFile.txt", "w")    
    for line in linea:
        if line != '\n':
            wFile.write(line)
    wFile.close()

    wbFile = open("profiletempFile.txt", 'a')  
    for line in lineb:
        if line != '\n':
            wbFile.write(line)
            
    wbFile.close()

    wcFile = open("profiletempFile.txt", 'a') 
    for line in linec:
        if line != '\n':
            wcFile.write(line)
    wcFile.close()

    wFile = open("MyCollege_profiles.txt", "w")  
    with open("profiletempFile.txt") as f:
        lines = ((line.split(None, 1)[:1], line) for line in f if line.strip())
        
        for k, g in groupby(lines, lambda L: L[0]):
            lines = [el[1] for el in g]
            lines.sort()
            for li in lines:
                wFile.write(li)
            wFile.write("=====" + '\n')
    wFile.close()



def output_users():
    aFile = open("accounts.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    wFile = open("MyCollege_users.txt", "w")    
    for line in lines:
        if line != '\n':
            wFile.write(line)
    wFile.close()

def output_training():
    wFile = open("MyCollege_training.txt", "w")  
    with open("learning.txt") as f:
        lines = ((line.split(None, 1)[:1], line) for line in f if line.strip())
        
        for k, g in groupby(lines, lambda L: L[0]):
            lines = [el[1] for el in g]
            lines.sort()
            for li in lines:
                wFile.write(li)
            wFile.write("=====" + '\n')
    wFile.close()

def home(user):
    output_jobs()
    output_userProfiles()
    output_users()
    output_training()

    a = ""
    login.play_story()

    while (a != "exit"):
        print("\nPlease type either: 'Login' or 'Register'. You can also press 0 for more options.")
        a = input("What would you like to do: ")
        if (a == "register" or a == "Register"):
            login.register()
            home('')
        elif (a == "Login" or a == "login"):
            login.login(user)
            home('')
        elif (a == "0"):

            b = ""

            while(b != '0'):
                print("")
                print("--------------------------------------------------------------------------")
                print("| Press '1' to find contacts that use InCollege.                         |")
                print("| Press '2' to see a video of a successful student who used InCollege!   |")
                print("| Press '3' to go to the 'Useful Links' page.                            |")
                print("| Press '4' to go to the 'InCollege Important Links' page.               |")
                print("| Press '5' to go to the 'Training' page.                                |")
                print("| Press '0' to return to the Home menu.                                  |")
                print("--------------------------------------------------------------------------")
                b = input("What would you like to do: ")

                if (b == '0'):
                    home('')
                elif (b == "1"):
                    login.contacts()
                elif (b == "2"):
                    login.play_video()
                elif (b == "3"):
                    usefulLinks.menu()
                elif(b == "4"):
                    importantLinks.Menu()
                elif b == "5":
                    training.training_menu()
                else:
                    print("Choose a valid option ")

        else:
            print("Choose a valid option ")
            home('')


if __name__ == "__home('')__":
    home('')

home('')
