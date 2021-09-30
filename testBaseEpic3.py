
def developers():
    underConstruction()

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")

def careers():
    underConstruction()

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")

def businessSolution():
    underConstruction()

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")
def directories():
    underConstruction()

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")

def blog():
    underConstruction()

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")

def underConstruction():
    print("")
    print("Page under construction.")
    print("")

def browseInCollege():
    underConstruction()

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")

def about():
    print("")
    print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
    print("")

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")

def press():
    print("")
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    print("")

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")


def register():
    print("register")

    '''
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

    file3.write(Fname + " " + Lname + "\n")

    file.close()
    file2.close()
    file3.close()

    nameofuser = Fname + " " + Lname
    print("\nHello, " + Fname)
    print("Account Created!")
    print("Entering main page....")
    mainPage(nameofuser)
    '''

def helpCenter():
    print("")
    print("We're here to help!")
    print("")

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")


def generalPage():
    print("")
    print("-----------------")
    print("|    General    |")
    print("-----------------")
    print("")
    print("Use the provided links for general information and commonly accessed pages.")
    print("Please choose from the following.")

    print("-----------------------------------------")
    print("| Press '1' to go to Sign Up.           |")
    print("| Press '2' to go to the Help Center.   |")
    print("| Press '3' to go to About.             |")
    print("| Press '4' to go to Press.             |")
    print("| Press '5' to go to Blog.              |")
    print("| Press '6' to go to Careers.           |")
    print("| Press '7' to go to Developers.        |")
    print("| Press '0' to return to previous menu. |")
    print("-----------------------------------------")
    print("")

    cmd = input("What would you like to do?: ")

    if (cmd == '0'):
            print("")
            #return

    elif (cmd == '1'):
        register()

    elif (cmd == '2'):
        helpCenter()

    elif (cmd == '3'):
        about()

    elif (cmd == '4'):
        press()

    elif (cmd == '5'):
        print("")
        blog()

    elif (cmd == '6'):
        careers()
        print("")

    elif (cmd == '7'):
        developers()
        #print("")

def menu():
    print("")
    print("---------------------")
    print("|    Useful Links   |")
    print("---------------------")
    print("")
    print("These links are provided by InCollege with your future in mind.")
    print("Please choose from the following.")

    cmd = ""
    #while (cmd != '0'):
    print("-----------------------------------------")
    print("| Press '1' for the General page.       |")
    print("| Press '2' to Browse InCollege.        |")
    print("| Press '3' for Business Solutions.     |")
    print("| Press '4' for Directories.            |")
    print("| Press '0' to return to previous menu. |")
    print("-----------------------------------------")
    print("")
    cmd = input("What would you like to do?: ")

    if (cmd == '0'):
        return
    elif (cmd == '1'):
        generalPage()

    elif (cmd == '2'):
        browseInCollege()

    elif (cmd == '3'):
        businessSolution()

    elif (cmd == '4'):
        directories()

    else:
        print("Invalid input, please try again.\n")


def home(user):
    a = ""
    #login.play_story()

    
    print("\nPlease type either: 'Login' or 'Register'. You can also press 0 for more options.")
    a = input("What would you like to do: ")
    if (a == "register" or a == "Register"):
        print("")
        #login.register()
        #home('')
    elif (a == "Login" or a == "login"):
        ##login.login(user)
        #home('')
        print("")
    elif (a == "0"):

        b = ""

            
    print("")
    print("--------------------------------------------------------------------------")
    print("| Press '1' to find contacts that use InCollege.                         |")
    print("| Press '2' to see a video of a successful student who used InCollege!   |")
    print("| Press '3' to go to the 'Useful Links' page.                            |")
    print("| Press '4' to go to the 'InCollege Important Links' page.               |")
    print("| Press '0' to return to the Home menu.                                  |")
    print("--------------------------------------------------------------------------")
    b = input("What would you like to do: ")

    if (b == '0'):
        home('')
    elif (b == "1"):
        #login.contacts()
        print("")
    elif (b == "2"):
        #login.play_video()
        print("")
    elif (b == "3"):
        #usefulLinks.menu()
        menu()
        #print("")
    else:
        print("Choose a valid option ")


