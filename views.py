#call after successfully login:

def mainPage():

    kbInput = "4"

    while(kbInput != "1" and kbInput != "2" and kbInput != "3"):
        print("")
        print("--------------------------------------------------------")
        print("InCollege")
        print("--------------------------------------------------------")
        print("Main page")
        print(" Enter page you want to go to: ")
        kbInput = input("   '1' to find someone you know, '2' for learn new skills, '3' for search for job, '4' to post a new job, '0' to return to login\n")
        if(kbInput == "1"):
            peopleSearchPage()
        elif(kbInput == "2"):
            skillsPage()
        elif(kbInput == "3"):
            jobSearchPage()
        elif(kbInput == "0"):
            from Users import home
            home('')
        elif(kbInput == 4):
            postNewJob()
        else:
            print("Please enter an available option!!\n")


def postNewJob():
    print("-----------------------------------")
    print(" Welcome to the Job Creation Page! ")
    print("-----------------------------------")


def peopleSearchPage():
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    file3 = open("accounts.txt", "r")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname
    
    from Users import find_contacts

    if (find_contacts(name)):
        print("They are a part of the InCollege system." + "\n")
        mainPage()
    else:
        print("They are not a part of the InCollege system" + "\n")
        mainPage()
    a = input("Press '0' to return.")
    if int(a) == 0:
        mainPage()

def skillsPage():
    kbInput = "6"

    while(kbInput != "1" and kbInput != "2" 
        and kbInput != "3" and kbInput != "4" and kbInput != "5" and kbInput != "b"):
        print("--------------------------------------------------------")
        print("Available skills to learn:")
        print("Enter the Coressponding Number with a skill to learn it today:")
        print(" 1. LeaderShip")
        print(" 2. Basic programming in Python")
        print(" 3. Make an outstanding resume")
        print(" 4. Professional writing")
        print(" 5. Microsoft Excel basics")
        kbInput = input(" Or enter b for return to mainPage\n")

        if(kbInput != "1" and kbInput != "2" 
        and kbInput != "3" and kbInput != "4" and kbInput != "5" and kbInput != "b"):
            print("Please enter the available options")
        elif(kbInput != "b"):
            print("Page under construction.")
            a = input("Press '0' to return")
            if int(a) == 0:
                mainPage()       
    

    if(kbInput == "b"):
        mainPage()
    
    
    
    

def jobSearchPage():
    print("Page under construction.")
    a = input("Press '0' to return.")
    if int(a) == 0:
        mainPage()

def pageUnderConstruction():
    print("")
    print("--------------------------------------------------------")
    print("Page under construction")


