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
    count = 0

    # Checks if there are already 5 accounts made this way
    for line in open("usernames.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted accounts have been created, please come backlater")
        home('')

    # Checks if there is a duplicate username
    u = input("Please enter a unique username: ")
    with open('usernames.txt') as f:
        if u in f.read():
            print("Error, Username already created! Returning home")
            home('')

    file.write(u + "\n")
    print(
        "Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
    p = input("Please enter a unique password: ")
    with open('passwords.txt') as f:
        if p in f.read():
            print("Error, Password already created! Returning home")
            home('')
    res = validatePass(p)
    print(res)
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
    file.close()
    file2.close()

    print("Account Created!")
    print("Entering main page....")
    mainPage()


def login(user):
    print("--------------------------")
    print("InCollege Login")
    print("--------------------------")
    file = open("usernames.txt", "a")
    file2 = open("passwords.txt", "a")

    u = input("Username: ")
    with open('usernames.txt') as f:
        if u in f.read():
            u = True
        else:
            flag = False

            while flag == False:
                with open('usernames.txt') as f:
                    if u in f.read():
                        break
                    else:
                        print("Error, Username is not recognized")
                        x = input("Enter username: ")
                        with open('usernames.txt') as f:
                            if x in f.read():
                                flag = True
                                break
                            else:
                                flag = False
    file.close()
    file2.close()

    p = input("Password: ")
    pas = validatePass(p)
    if pas is True:
        mainPage()
    else:
        while pas is False:
            print("Error, Incorrect password")
            p = input("Enter password: ")
            if validatePass(p):
                break
        mainPage()


if __name__ == "__home('')__":
    home('')
