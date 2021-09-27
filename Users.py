import random
from views import mainPage
from validatePass import validatePass
import login


class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home(user):
    a = ""
    login.play_story()
    print("\nPlease type either: 'Login' or 'Register'. You can also press 0 for more options.")
    a = input("What would you like to do: ")
    if (a == "register" or a == "Register"):
        login.register()
        home('')
    elif (a == "Login" or a == "login"):
        login.login(user)
        home('')
    elif (a == "0"):
        print("\nPress '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!")
        b = input("What would you like to do: ")

        if (b == "1"):
            login.play_video()
            home('')
        elif (b == "0"):
            login.contacts()
            home('')
        else:
            print("Choose a valid option ")
            home('')
    else:
        print("Choose a valid option ")
        home('')


if __name__ == "__home('')__":
    home('')

home('')
