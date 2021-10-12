import login


def menu():
    print("")
    print("---------------------")
    print("|    Useful Links   |")
    print("---------------------")
    print("")
    print("These links are provided by InCollege with your future in mind.")
    print("Please choose from the following.")

    cmd = ""
    while (cmd != '0'):
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


def generalPage():
    print("")
    print("-----------------")
    print("|    General    |")
    print("-----------------")
    print("")
    print("Use the provided links for general information and commonly accessed pages.")
    print("Please choose from the following.")

    cmd = ""
    while (cmd != '0'):
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
            return

        elif (cmd == '1'):
            login.register()

        elif (cmd == '2'):
            helpCenter()

        elif (cmd == '3'):
            about()

        elif (cmd == '4'):
            press()

        elif (cmd == '5'):
            blog()

        elif (cmd == '6'):
            careers()

        elif (cmd == '7'):
            developers()

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


def underConstruction():
    print("")
    print("Page under construction.")
    print("")