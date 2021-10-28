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
        print("| '1' to open inbox                      |")
        print("| '2' to message a friend                |")
        print("| '0' to return to main page             |")
        print("------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            inbox(username)
        elif (cmd == '2'):
            messageFriend(username)
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")

def inbox(username):
    inbox = []
    file = open("mailboxDataBase.txt", "r")

    lines = file.readlines()
    file.close()
    r = "TO:: " + username
    for line in lines:
        if r in line:
            inbox.append(line)
    
    print(inbox)


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
        
       
        if cmd ==  fu or u:
            with open('accounts.txt','r') as f:
                if cmd in f.read():
                    sendMessage(cmd)
                    return

        if (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")
    
    
def sendMessage(friend):
    m = input("Please enter the message you want to send to "+ friend +":")

    file = open("mailboxDataBase.txt", "a")
    file.write("TO:: " +friend + ": "+ m + " From::" + user +"\n")