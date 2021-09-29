import usefulLinks

def importantLinksMenu():
    print("\n------------------------")
    print("| Important Links Menu |")
    print("------------------------\n")
    print("Please choose from the following.\n")

    selection = ""
    while (selection != "0"):
        print("-----------------------------------------")
        print("| Press '1' for the Copyright Notice.     |")
        print("| Press '2' for About.                    |")
        print("| Press '3' for Accessibility.            |")
        print("| Press '4' for the User Agreement.       |")
        print("| Press '5' for the Privacy Policy.       |")
        print("| Press '6' for the Cookie Policy.        |")
        print("| Press '7' for the Copyright Policy.     |")
        print("| Press '8' for the Brand Policy.         |")
        print("| Press '9' for the Guest Controls.       |")
        print("| Press '10' for Languages.        |")
        print("| Press '0' to return to previous menu.   |")
        print("-----------------------------------------")
        print("")

    if (selection == "0"):
        return

    elif (selection == 1):
        copyrightNotice()
    
    elif (selection == 2):
        usefulLinks.about()
    
    elif (selection == 3):
        accessibility()
    
    elif (selection == 4):
        userAgreement()
    
    elif (selection == 5):
        privacyPolicy()
    
    elif (selection == 6):
        cookiePolicy()
    
    elif (selection == 7):
        copyrightPolicy()
    
    elif (selection == 8):
        brandPolicy()
    
    elif (selection == 9):
        guestControls()
    
    elif (selection == "10"):
        languages()
    
    else:
        print("Invalid input, please try again.\n")


def copyrightNotice():
    print("")


def accessibility():
    print("")


def userAgreement():
    print("")


def privacyPolicy():
    print("")


def cookiePolicy():
    print("")


def copyrightPolicy():
    print("")


def brandPolicy():
    print("")


def guestControls():
    print("")


def languages():
    print("")