import random

import usefulLinks
from views import mainPage
from validatePass import validatePass
import login
import importantLinks
import training
import outputApi
import epic10

class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home(user):
    epic10.newJobsAPI()
    epic10.studentAccountAPI()
    epic10.trainingAPI()
    outputApi.output_jobs()
    outputApi.output_userProfiles()
    outputApi.output_users()
    outputApi.output_training()
    outputApi.output_savedJobs()
    
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
