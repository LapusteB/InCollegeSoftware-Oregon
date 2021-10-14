class Friend:
    def __init__(self, username, friend_username):
        self.username = username
        self.friend_username = friend_username
    
    def __eq__(self, other):
        return self.friend_username == other.friend_username

def friendMenu(username):
    global requested_friendList, user
    requested_friendList = []
    
    user = username
    requestFile = open("friend_requested.txt", "r")
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            temp = Friend(u, fu)
            requested_friendList.append(temp)
    requestFile.close()

    show_network(username)
    cmd = ""
    while(cmd != "0"):
                
        print("")
        print("------------------------------------------")
        print("| '1' to show your network               |")
        print("| '2' to search people and send request  |")
        print("| '3' to disconnect network              |")
        print("| '0' to return to main page             |")
        print("------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            show_network(username)
        elif (cmd == '2'):
            addFriends(username)
        elif (cmd == '3'):
            disconnect_network(username)
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")
      
        fn = open('friend_requested.txt', 'r+')
        fn.truncate(0)

        for rel in requested_friendList:
            requestFileWrite = open("friend_requested.txt", 'a')
            
            requestFileWrite.write(rel.username + '\t' +
                                    rel.friend_username + '\n')
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
                    temp = Friend(username, last_username)
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
    global last_username
    for line in open("profile.txt", "r"):
        if line != '\n':
            u, t, m, n, a = line.split('\t')
            
            first, last= u.split(' ')
            if(last == input_last and u != user):
                last_username = u
                return True
    return False

def has_user_uni(input_uni):
    global uni_username
    for line in open("profile.txt", "r"):
        if line != '\n':
            u, t, m, n, a = line.split('\t')
            
            if(n == input_uni+' ' and u != user):
                uni_username = u
                return True
    return False

def has_user_maj(input_maj):
    global maj_username
    for line in open("profile.txt", "r"):
        if line != '\n':
            u, t, m, n, a = line.split('\t')
            
            if(m == input_maj + ' ' and u != user):
                maj_username = u
                return True
    return False

def show_network(username):
    count_pending = 0
    print("Your pending friend requests:\n")
    requestFile = open("friend_requested.txt", "r")
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username):
                count_pending += 1
                print("Waiting friend reuqest response from: " + fu)
    requestFile.close()  

    if(count_pending == 0):
        print("No pending friend requests")

    count_friend = 0
    print("Your friends:\n")
    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username or fu == username + '\n'):
                count_friend += 1
                if(u == username):
                    print("Friend username: " + fu)
                else:
                    print("Friend username: " + u)
    friendFile.close()    
    if(count_friend == 0):
        print("No friend to show")

def disconnect_network(username):
    print("Your friends:\n")
    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            
            if (u == username or fu == username + '\n'):
                if(u == username):
                    print("Friend username: " + fu)
                else:
                    print("Friend username: " + u)
    friendFile.close() 

    aFile = open("friendList.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    delete = input("Which user would you like to be disconnected? ")
    if(has_delete_user(delete, username) == False):
        print("The user is not friend with you")
        return

    wFile = open("friendList.txt", "w")
    for line in lines:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username and fu == delete +'\n'):
                
                print(fu + " has been disconnected from your friend list ")
                break
            elif(u == delete and fu == username + '\n'):
                
                print(u + " has been disconnected from your friend list ")
                break
            else:
                wFile.write(line)
    wFile.close() 
    

def has_delete_user(delete, username):
    friendFile = open("friendList.txt", "r")
    for line in friendFile:
        if line != '\n':
            u, fu = line.split('\t')
            if (u == username and  fu == delete + '\n'):
                return True
            elif(u == delete and fu == username + '\n'):
                return True             
    friendFile.close() 
    return False  

def has_pending_requests(username):
    
    aFile = open("friend_requested.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    wFile = open("friend_requested.txt", "w")    
    for line in lines:
        if line != '\n':
            u, fu = line.split('\t')
            
            if(fu == username + '\n'):
                print("You have pending friend requests from " + u)
                decision = input("Would you like to accept or reject the request? ")
                if(decision == "accept" or decision == "Accept"):
                    friendFileWrite = open("friendList.txt", 'a')
            
                    friendFileWrite.write(u + '\t' +
                                    username + '\n')
                    friendFileWrite.close()
                    
                    print("Friend request has been successfully accepted")
                elif(decision == "reject" or decision == "Reject"):
                    
                    print("Friend request has been successfully rejected")
            else:
                wFile.write(line)
    wFile.close()