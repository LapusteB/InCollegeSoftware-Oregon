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
    file = open("usernames.txt", "a") # - file will be created if not present
    count = 0

 #Checks if there are already 5 accounts made this way
    for line in open("usernames.txt", "r"): count += 1 
    if count == 5:
        print("All permitted accounts have been created, please come backlater")
        home('')

 #Checks if there is a duplicate username
    u = input("Please enter a unique username: ")
    with open('usernames.txt') as f: 
        if u in f.read():
            print("Error, Username already created! Returning home")
            home('')

    file.write(u + "\n")


def login(user):
    mainPage()
    #TO DO


        
home('')