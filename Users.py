from views import mainPage
from validatePass import validatePass

class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home(user):
    print("Please type either: 'Login' or 'Register")
    a = input("What would you like to do: ")
    if(a == "register" or a == "Register"):
        register()
    elif(a == "Login" or a == "login"):
        login(user)
    else:
        print("Choose a valid option")
        home('')

#'r'- open a file for reading, 'w' - open a file for writing, '+' open a file for reading and writing
def register():
    print("-----------------------------")
    print("Welcome to the InCollege App!")
    print("-----------------------------")
    u = input("Please enter a unique username: ")
    file = open("dataBase.txt", "w")
    file.write(u)
    
    #TO DO


def login(user):
    mainPage()
    #TO DO


        
home('')