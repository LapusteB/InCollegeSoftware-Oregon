class Friend:
    def __init__(self, username, friend_lastname):
        self.username = username
        self.friend_lastname = friend_lastname

def friendMenu(username):
    global friends, requested_friendList, user
    requested_friendList = []
    user = username
    addFriends(username)
    show_network(username)
    disconnect_network(username)

    fn = open('friend_requested.txt', 'r+')
    fn.truncate(0)

    for rel in requested_friendList:
        requestFileWrite = open("friend_requested.txt", 'a')
        
        requestFileWrite.write(rel.username + '\t' +
                                rel.friend_lastname + '\n')
        requestFileWrite.close()

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

def addFriends(username):
    keep = "y"
    while(keep == "y" or keep == "Y"):
        search_by = input("Would you like to search students by lastname, university, or major? ")
        
        if(search_by == "lastname" or search_by == "Lastname"):
            input_last = input("What is the last name you would like to search? ")
                        
            if(has_user_last(input_last)):
                request = input("User with that last name exists. Would you like to send friend request?(y/n) ")                    
                if(request == 'y'):
                    temp = Friend(username, input_last)
                    requested_friendList.append(temp)
                    print("Friend request has been sent")
                    keep = input("Would you like to continue search?(y/n) ")
                    
                elif(request == 'n'):
                    print("You've decided not to send friend request\n")
                    keep = input("Would you like to continue search?(y/n) ")
                    
                else:
                    print("You will be able to search by lastname, university or major only.")
                    keep = input("Would you like to continue search?(y/n) ")
                    
            else:
                print("No user with that last name found")
                keep = input("Would you like to continue search?(y/n) ")

        elif(search_by == "university" or search_by == "University"):
            input_uni = input("What is the university you would like to search? ")

            if(has_user_uni(input_uni)):
                request = input("User with that university exists. Would you like to send friend request?(y/n) ")                    
                if(request == 'y'):
                    temp = Friend(username, uni_username)
                    requested_friendList.append(temp)
                    print("Friend request has been sent")
                    keep = input("Would you like to continue search?(y/n) ")
                    
                elif(request == 'n'):
                    print("You've decided not to send friend request\n")
                    keep = input("Would you like to continue search?(y/n) ")
                    
                else:
                    print("You will be able to search by lastname, university or major only.")
                    keep = input("Would you like to continue search?(y/n) ")

        elif(search_by == "major" or search_by == "Major"):
            input_maj = input("What is the major you would like to search? ")

            if(has_user_maj(input_maj)):
                request = input("User with that major exists. Would you like to send friend request?(y/n) ")                    
                if(request == 'y'):
                    temp = Friend(username, maj_username)
                    requested_friendList.append(temp)
                    print("Friend request has been sent")
                    keep = input("Would you like to continue search?(y/n) ")
                    
                elif(request == 'n'):
                    print("You've decided not to send friend request\n")
                    keep = input("Would you like to continue search?(y/n) ")
                    
                else:
                    print("You will be able to search by lastname, university or major only.")
                    keep = input("Would you like to continue search?(y/n) ")
        else:
            print("Invalid input")
            keep = input("Would you like to continue search?(y/n) ")

def has_user_last(input_last):
    
    for line in open("profile.txt", "r"):
        if line != '\n':
            u, t, m, n, a = line.split('\t')
            first, last= u.split(' ')
            if(last == input_last):
                return True
    return False

def has_user_uni(input_uni):
    global uni_username
    for line in open("profile.txt", "r"):
        if line != '\n':
            u, t, m, n, a = line.split('\t')
            if( n == input_uni):
                uni_username = u
                return True
    return False

def has_user_maj(input_uni):
    global maj_username
    for line in open("profile.txt", "r"):
        if line != '\n':
            u, t, m, n, a = line.split('\t')
            if( n == input_uni):
                maj_username = u
                return True
    return False

def show_network(username):
    print("Your pending friend requests:\n")
    requestFile = open("friend_requested.txt", "r")
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username):
                print("Waiting friend reuqest response from: " + fu)
    requestFile.close()  

    print("Your friends:\n")
    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username or fu == username):
                if(u == username):
                    print("Friend username: " + fu)
                else:
                    print("Friend username: " + u)
    friendFile.close()    

def disconnect_network(username):
    print("Your friends:\n")
    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username or fu == username):
                if(u == username):
                    print("Friend username: " + fu)
                else:
                    print("Friend username: " + u)
    friendFile.close() 

    delete = input("Which user would you like to be disconnected? ")
    if(has_delete_user(delete) == False):
        print("The user is not friend with you")
        return

    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username and fu == delete):
                del line
                print(fu + " has been disconnected from your friend list ")
                break
            elif(u == delete and fu == username):
                del line
                print(u + " has been disconnected from your friend list ")
                break
            
    friendFile.close() 

def has_delete_user(delete):
    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == user and  fu == delete):
                return True
            elif(u == delete and fu == user):
                return True             
    friendFile.close() 
    return False  
