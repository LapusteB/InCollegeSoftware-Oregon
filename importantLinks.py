import usefulLinks

def Menu():
    print("\n------------------------")
    print("| Important Links Menu |")
    print("------------------------\n")
    print("Please choose from the following.\n")

    selection = ''
    while (selection != '0'):
        print("-------------------------------------------")
        print("| Press '1' for the Copyright Notice.     |")
        print("| Press '2' for About.                    |")
        print("| Press '3' for Accessibility.            |")
        print("| Press '4' for the User Agreement.       |")
        print("| Press '5' for the Privacy Policy.       |")
        print("| Press '6' for the Cookie Policy.        |")
        print("| Press '7' for the Copyright Policy.     |")
        print("| Press '8' for the Brand Policy.         |")
        print("| Press '9' for the Guest Controls.       |")
        print("| Press '10' for Languages.               |")
        print("| Press '0' to return to previous menu.   |")
        print("-------------------------------------------")
        selection = input("Enter the page you want to go to: ")

        if (selection == '0'):
            return

        elif (selection == '1'):
            copyrightNotice()
        
        elif (selection == '2'):
            usefulLinks.about()
        
        elif (selection == '3'):
            accessibility()
        
        elif (selection == '4'):
            userAgreement()
        
        elif (selection == '5'):
            privacyPolicy()
        
        elif (selection == '6'):
            cookiePolicy()
        
        elif (selection == '7'):
            copyrightPolicy()
        
        elif (selection == '8'):
            brandPolicy()
        
        elif (selection == '9'):
            guestControls()
        
        elif (selection == '10'):
            languages()
        
        else:
            print("Invalid input, please try again.\n")


def copyrightNotice():
    print("")
    print("--------------------------")
    print("|    Copyright Notice    |")
    print("--------------------------")

    cmd = ""

    print("\nCopyright 2021, Team Oregon. All rights reserved.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def accessibility():
    print("")
    print("-----------------------")
    print("|    Accessibility    |")
    print("-----------------------")

    cmd = ""

    print("\nInCollege is accessible in the following ways:")
    print("1. Clear headings are used to organize the structure of the content clearly.")
    print("2. Text-based so color does not affect the experience of the user.")
    print("3. All links have unique and descriptive names for easier navigation.")
    print("4. All content can be accessed using the keyboard alone.")
    print("5. No dynamic content, making it easy for screen readers to navigate the application.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def userAgreement():
    print("")
    print("------------------------")
    print("|    User Agreement    |")
    print("------------------------")
    
    cmd = ""

    print("\nWelcome, and thanks for using InCollege!")
    print("Please take a minute and read over the user agreement.")

    print("\nThis agreement is a legal contract between you and us.")
    print("You acknowledge that you have read and understood the terms of this agreement.")
    print("If you do not agree to the terms of this agreement, you should not use InCollege.")
    print("We may, at any time, terminate your account or priviledges for violations of this agreement.")

    print("\nIntellectual Property")
    print("Team Oregon owns all rights, titles, and interest in and to this application.")
    print("You may not modify, adapt, translate, decompile, or attempt to retrieve source code from this application.")
    
    print("\nPrivacy")
    print("We will not use or sell your information to external entities.")
    print("When you use InCollege you can be confident that your private information is safe from external attacks.")
    print("When you make a post on InCollege, be aware that this is public and it may be seen by other users, or non-users of this application.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def privacyPolicy():
    print("")
    print("------------------------")
    print("|    Privacy Policy    |")
    print("------------------------")

    cmd = ""

    print("\nWhen you use InCollege, you may give us certain information voluntarily.")
    print("This includes your name, employer, location, and any other information you give us.")

    print("\nWe utilize this information to create a more personalized experience for you, the user.")
    print("This information will not be sold or given to any external entities.")

    print("\nPlease note that any personal information posted publicly and voluntarily, may be seen by others.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def cookiePolicy():
    print("")
    print("-----------------------")
    print("|    Cookie Policy    |")
    print("-----------------------")

    cmd = ""

    print("\nThis application does not currently utilize cookies.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def copyrightPolicy():
    print("")
    print("--------------------------")
    print("|    Copyright Policy    |")
    print("--------------------------")

    cmd = ""

    print("\nWe at Team Oregon recognize and respect intellectual property rights and are committed to ")
    print("fulfilling our moral and legal obligations with respect to our use of copyright-protected works.")

    print("\nTeam Oregon expects its employees to be responsible when consuming copyrighted materials.")
    print("Employees who duplicate copyrighted works may be subject to termination, or other disciplinary actions.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def brandPolicy():
    print("")
    print("----------------------")
    print("|    Brand Policy    |")
    print("----------------------")

    cmd = ""

    print("\nEntities may only use InCollege trademarks in strict accordance with this policy.")
    
    print("\nNo entity may alter or combine InCollege trademarks with any other elements.")
    print("The use of InCollege icons, graphics, or logos without direct permission from Team Oregon, is not allowed.")
    print("The use of InCollege trademarks for commercial merchandise is prohibited.")

    while (cmd != '0'):
        cmd = input("\nPress '0' to return to previous page: ")

    if (cmd == '0'):
        return

    else:
        print("")
        print("Invalid input, please try again.")


def guestControls():
    print("")
    print("------------------------")
    print("|    Guest Controls    |")
    print("------------------------")

    selection = ""
    with open('controls.txt', 'r') as file:
        preferences = file.readlines()

    print("\nYour current preferences are: ")
    print("Email: " + preferences[0])
    print("SMS: " + preferences[1])
    print("Targeted Advertising: " + preferences[2])
    
    cmd = ''
    while(cmd != '0' and cmd != '1'):
        cmd = input("Press '0' to return to previous page or '1' to edit your preferences: ")
    
        if (cmd == '0'):
            return
        
        elif(cmd == '1'):
            systemPreferences(preferences)

        else:
            print("")
            print("Invalid input, please try again.")


def systemPreferences(preferences):
    change = ""
    while(change != '0'):
        change = input("To change your preferences, press '1' for email, '2' for SMS, '3' for Targeted Advertising, or '0' to quit: ")

        if (change == '0'):
            with open('controls.txt', 'w') as file:
                file.writelines(preferences)
            print("")
            return
        
        elif (change == '1'):
            if (preferences[0] == "off\n"):
                preferences[0] = "on\n"
            else:
                preferences[0] = "off\n"
            
            print("Your email preferences have been turned " + preferences[0])
        
        elif (change == '2'):
            if (preferences[1] == "off\n"):
                preferences[1] = "on\n"
            else:
                preferences[1] = "off\n"
            
            print("Your SMS preferences have been turned " + preferences[1])

        elif (change == '3'):
            if (preferences[2] == "off"):
                preferences[2] = "on"
            else:
                preferences[2] = "off"
            
            print("Your Targeted Advertising preferences have been turned " + preferences[2])
        
        else:
            print("")
            print("Invalid input, please try again.")


def languages():
    print("")
    print("-------------------")
    print("|    Languages    |")
    print("-------------------")
    
    with open('language.txt', 'r') as file:
        lang = file.readlines()

    newLanguage = ""

    print("Welcome, your current application language is " + lang[0] + ".\n")

    while (newLanguage != '1'and newLanguage != '2' and newLanguage != '0'):
        if (lang[0] == "English"):
            newLanguage = input("Select '2' to change language to Spanish, or '0' to quit: ")
        
        elif(lang[0] == "Spanish"):
            newLanguage = input("Select '1' to change language to English, or '0' to quit: ")

        if (newLanguage == '1'):
            lang[0] = "English"
        
        elif(newLanguage == '2'):
            lang[0] = "Spanish"
        
        elif (newLanguage == '0'):
            return
        
        else:
            print("")
            print("Invalid input, please try again.")
    
    with open('language.txt', 'w') as file:
        file.writelines(lang)

    cmd = ""
    while (cmd != '0'):
        cmd = input("Press '0' to return to previous page: ")

        if (cmd == '0'):
            return

        else:
            print("")
            print("Invalid input, please try again.")