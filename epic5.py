def friendList(username):
    open("friendList.txt","r")
    
    friends= []

    print(friends)

    for i in range(len(friends)):
        if hasProfile(friends[i]):
            print(friends[i] + "profile")
        else: print(friends[i])
    
    userInput = input("enter the friend name with profile to see profile")
    
    for i in range(len(friends)):
        if userInput == friends[i]: 
            showProfile(friends[i])
        else: print(friends[i] + "does not have profile yet")



def showProfile(username):
    print("Profile:")


def hasProfile(username):
    if hasProfile == True: 
        return True
    else: return False

