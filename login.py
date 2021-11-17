from validatePass import validatePass
from views import mainPage
import notifications
import random
#from Users import output_users

def login(user):
    print("--------------------------")
    print("InCollege Login")
    print("--------------------------")
    file = open("usernames.txt", "a")
    file2 = open("passwords.txt", "a")
    file3 = open("accounts.txt", "a")
    indexU = 0

    filename = "usernames.txt"
    with open(filename) as file:
        linesU = file.readlines()
        linesU = [line.rstrip() for line in linesU]

    filename = "passwords.txt"
    with open(filename) as file:
        linesP = file.readlines()
        linesP = [line.rstrip() for line in linesP]

    print("(Press '0' to return)")
    u = input("Username:")
    with open('usernames.txt') as f:
        if u in f.read():
            indexU = linesU.index(u)
            u = True
        elif u == "0":
            return
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
    with open('accounts.txt') as file:
        linesN = file.readlines()
    name = linesN[indexU]
    file.close()
    file2.close()
    file3.close()

    global login_name
    login_name = name.strip()

    p = input("Password: ")

    if p == linesP[indexU]:
        mainPage(login_name)
    else:
        while p != linesP[indexU]:
            print("Error, Incorrect password")
            p = input("Enter password: ")
            if p == linesP[indexU]:
                break
        mainPage(login_name)

    return


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
        return

    # Checks if there is a duplicate username
    print("(Press '0' to return)")
    u = input("Please enter a unique username: ")
    if username_exists(u):
        print("Error, Username already created! Returning home")
        return

    if u == "0":
        return

    
    file.write(u + "\n")
    print(
        "Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
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

    print("-------------------------------------------------")
    plus = input("- Do you want to register as a PLUS member? (y/n): ")
    if plus == "y":
        Fname = Fname + "++"
    print("-------------------------------------------------")
    
    file3.write(Fname + " " + Lname + "\n")

    file.close()
    file2.close()
    file3.close()

    output_users()
    nameofuser = Fname + " " + Lname
    
    print("\nHello, " + Fname)
    print("Account Created!")
    print("Entering main page....")
    notifications.addNotificationsForNewUser(Fname, Lname)
    mainPage(nameofuser)


def contacts():
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname

    if (find_contacts(name)):
        print("")
        print("They are a part of the InCollege system. Register or login now to join them!" + "\n")
        return
    else:
        print("")
        print("They are not a part of the InCollege system")
        no_contacts = input("Press '0' to return to login/register page or '1' to search again.")
        if (no_contacts == "0"):
            return
        elif (no_contacts == "1"):
            contacts()


def has_max_users():
    count = 0
    for line in open("usernames.txt", "r"): count += 1
    if count == 10 or count > 10:
        print("All permitted accounts have been created, please come backlater")
        return True
    return False


def username_exists(u):
    with open('usernames.txt') as f:
        if u in f.read():
            return True
        return False


def play_video():
    print("Video is now playing\n")
    a = ""

    while(a != "0"):
        a = input("Press '0' for home.")
        if (a == "0"):
            return
        else:
            print("Invalid input, please try again\n")



def play_story():
    print("")
    print("**********************************************************************************************")
    n = random.randint(1, 3)
    if n == 1:
        story_1()
    elif n == 2:
        story_2()
    elif n == 3:
        story_3()
    print("**********************************************************************************************")
    print("")


def story_1():
    return print("* John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD. *\n" +
                 "* I loved computers. I taught myself to program in high school,                              *\n" +
                 "* and thought I was pretty good at it (Apple Basic and 6502 assembler)                       *\n" +
                 "* by the time I graduated. I got a job typesetting at a newspaper,                           *\n" +
                 "* and enrolled in university part time, taking programming classes.                          *")


def story_2():
    return print("* Hazim Hardeman, Communications Program Graduate, 2015                                      *\n" +
                 "* When Hazim Hardeman started at Community College of Philadelphia in 2012, his goals were   *\n" +
                 "* to raise his GPA and transfer to Temple University. He accomplished that and much more,    *\n" +
                 "* graduating from the College in 2015 with an associate degree in Communications with        *\n" +
                 "* High Honors.                                                                               *")


def story_3():
    return print("* Mark Zuckerberg has already accomplished much in his short life. In 2004,                  *\n" +
                 "* he launched Facebook with a handful of his fellow college students, and 10 years later, the*\n" +
                 "* website has more than 1 billion active users around the globe, and more than $12 billion   *\n" +
                 "* in annual revenues. 'Helping a billion people connect is amazing, humbling and by far the   *\n" +
                 "* thing I am most proud of in my life.'                                                       *")


def find_contacts(n):
    with open('accounts.txt') as f:
        if n in f.read():
            return True
        return False


def output_users():
    aFile = open("accounts.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    wFile = open("MyCollege_users.txt", "w")
    for line in lines:
        if line != '\n':
            wFile.write(line)
    wFile.close()
