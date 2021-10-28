import friendList
from profile import Profile
import profile as p1
import profile
from friend import Friend

class Mailbox:
    def __init__(self, username, friend_username):
        self.username = username
        self.friend_username = friend_username
    
    def __eq__(self, other):
        return self.friend_username == other.friend_username

def mailboxMenu(username):
    global user
    user = username
    print("----------Welcome to mailbox-------------")

    cmd = ""
    while(cmd != "0"):
                
        print("")
        print("------------------------------------------")
        print("| '1' to open mailbox                    |")
        print("| '2' to message a friend                |")
        print("| '0' to return to main page             |")
        print("------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            print("...")
        elif (cmd == '2'):
            messageFriend(username)
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")

def messageFriend(username):
    
    profileExists = False

    friendWithProfileCount = -1
    friendWithProfileMap = {}

    count_friend = -1
    print("-------------------------------------")
    print("| Friend List                       |")
    
    friendFile = open("friendList.txt", "r")
    
    for line in friendFile:
        if line != '\n':
            line = line.rstrip()
            u, fu = line.split('\t')

            if (u == username or fu == username):
                count_friend += 1

                if(u == username):
                    #check if has profile: 
                    profileFile = open("profile.txt", "r")
                    for line in profileFile:
                        if line != '\n':
                            a, t, n, m, p = line.split('\t')
                            profile = Profile(a, t, n, m, p)
                            if (str(profile.name) == str(fu)):
                                profileExists = True
                                friendWithProfileCount +=1

                    profileFile.close()
                    if(profileExists):
                        friendWithProfileMap[friendWithProfileCount] = {fu}
                        print("    Friend name: " + fu + ", "+ str(friendWithProfileCount) +"(has profile)")
                    else: print("    Friend name: " + fu)
                else:
                    #check if friend has profile
                    profileFile = open("profile.txt", "r")
                    for line in profileFile:
                        if line != '\n':
                            a, t, n, m, p = line.split('\t')
                            profile = Profile(a, t, n, m, p)
                            if (str(profile.name) == str(u)):
                                friendWithProfileCount +=1
                                profileExists = True
                    profileFile.close()
                    if(profileExists):
                        friendWithProfileMap[friendWithProfileCount] = {u}
                        print("    Friend name: " + u  + ", "+ str(friendWithProfileCount) +"(has profile)")
                    else: print("    Friend name: " + u)
                
        profileExists = False


    if(count_friend == -1):
        print("| No friend to show                 |")
        print("-------------------------------------")
        friendFile.close() 
    else:
        profileInputSelect = "0"
        
    
    cmd = ""
    while(cmd != "0"):
                
        print("")
        print("| '0' to return to main page             |")   
        cmd = input("| Enter the name of your friend you want to message: ")
        
       
        

        if (cmd == '1'):
            print("...")
        elif (cmd == '2'):
            messageFriend(username)
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")
    
    '''
    from friendList import friendList1
    friendList1(username)
    '''
    
    