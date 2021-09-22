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
    if (a == "register" or a == "Register"):
        register()
    elif (a == "Login" or a == "login"):
        login(user)
    else:
        print("Choose a valid option")
        home('')


# 'r'- open a file for reading, 'w' - open a file for writing, '+' open a file for reading and writing
def register():
    print("-----------------------------")
    print("Welcome to the InCollege App!")
    print("-----------------------------")
    file = open("usernames.txt", "a")  # - file will be created if not present
    file2 = open("passwords.txt", "a")  # - file will be created if not present
    file3 = open("accounts.txt", "a")
    # Checks if there are already 5 accounts made this way
    if has_max_users():
        home('')

    # Checks if there is a duplicate username
    u = input("Please enter a unique username: ")
    if username_exists(u):
        print("Error, Username already created! Returning home")
        home('')

    file.write(u + "\n")
    print("Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
    p = input("Please enter a valid password: ")
    res = validatePass(p)

    while res is False:
        if res is False:
            print("Error, Please meet password requirements:")
            print("---------------------------------------------")
            print("-minimum of 8 characters")
            print("-maximum of 12 characters")
            print("-at least one capital letter")
            print("-one digit, one non-alpha character")
            print("---------------------------------------------")
        p = input("Re-enter Password: ")
        res = validatePass(p)
    file2.write(p + "\n")
    Fname = input("What is your first name?: ")
    Lname = input("What is your last name?: ")

    file3.write(Fname + " " + Lname + "\n")

    file.close()
    file2.close()
    file3.close()
   

    print("\nHello, " + Fname)
    print("Account Created!")
    print("Entering main page....")
    mainPage()


def login(user):
    print("--------------------------")
    print("InCollege Login")
    print("--------------------------")
    file = open("usernames.txt", "a")
    file2 = open("passwords.txt", "a")
    indexU = 0
    

    filename = "usernames.txt"
    with open(filename) as file:
        linesU = file.readlines()
        linesU = [line.rstrip() for line in linesU]

    filename = "passwords.txt"
    with open(filename) as file:
        linesP = file.readlines()
        linesP = [line.rstrip() for line in linesP]

    u = input("Username: ")
    with open('usernames.txt') as f:
        if u in f.read():
            indexU = linesU.index(u)
            u = True
          
        else:
            flag = False
            while flag == False:
                with open('usernames.txt') as f:
                    if u in f.read():
                        indexU = linesU.index(u)
                        break
                    else:
                        print("Error, Username is not recognized")
                        x = input("Enter username: ")
                        with open('usernames.txt') as f:
                            if x in f.read():
                                indexU = linesU.index(u)
                                flag = True
                                break
                            else:
                                flag = False
    file.close()
    file2.close()

    p = input("Password: ")
    flag = validatePass(p)


    if p == linesP[indexU]:
        mainPage()
    else:
        while p != linesP[indexU]:
            print("Error, Incorrect password")
            p = input("Enter password: ")
            if p == linesP[indexU]:
                break
        mainPage()

#def Get_or_find account():

def has_max_users():
    count = 0
    for line in open("usernames.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted accounts have been created, please come backlater")
        return True
    return False


def username_exists(u):
    with open('usernames.txt') as f:
        if u in f.read():
            return True
        return False


if __name__ == "__home('')__":
    home('')

home('')
