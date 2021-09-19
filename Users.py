from views import mainPage
from validatePass import validatePass
from register import register


class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home():
    print("Please type either: 'Login' or 'Register")
    a = input("What would you like to do: ")
    if (a == "register" or a == "Register"):
        register()
    elif (a == "Login" or a == "login"):
        login()
    else:
        print("Choose a valid option")
        home()












#if __name__ == "__home('')__":
#    home('')

home()
