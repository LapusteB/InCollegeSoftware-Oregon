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
        kbInput = input("   1 to find someone you know, 2 for learn new skills, 3 for search for job\n")
        if(kbInput == "1"):
            peopleSearchPage()
        elif(kbInput == "2"):
            skillsPage()
        elif(kbInput == "3"):
            jobSearchPage()
        else:
            print("Please enter an available option!!\n")


def peopleSearchPage():
    pageUnderConstruction()

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
    

    if(kbInput == "b"):
        mainPage()
    
    
    
    

def jobSearchPage():
    pageUnderConstruction()

def pageUnderConstruction():
    print("")
    print("--------------------------------------------------------")
    print("Page under construction")


