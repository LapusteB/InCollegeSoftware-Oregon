#call after successfully login
def mainPage():
    print("Hello:")
    print("Enter page you want to go to: ")
    a = input("1 to search for people you know, 2 for learn new skills, 3 for search for job")
    if( a == '1'):
        peopleSearchPage()
    elif(a == '2'):
        skillsPage()
    elif( a == '3'):
        jobSearchPage()


def peopleSearchPage():
    print("Page under construction")

def skillsPage():
    print("Page under construction")

def jobSearchPage():
    print("Page under construction")

#from 3 above options
def backToMainPage():
    print("Page under construction")
