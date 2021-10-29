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
            if (isPlus(username)):
                messageUser(username)
            else:
                messageFriend((username))
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")

def inbox(username):
    count = 0
    inbox = []
    file = open("mailboxDataBase.txt", "r")

    lines = file.readlines()
    file.close()
    r = "TO:: " + username
    for line in lines:
        if r in line:
            inbox.append(line)

    print(inbox)

    inp = ''
    while inp != '0' or inp != 'Reply' or inp != 'reply' or inp != 'Manage' or inp != 'manage':
        inp = input("Would you like to manage your inbox or reply to a message? (Type 'reply', 'manage', or 0 to exit)")
        if inp == 'Reply' or inp == 'reply':
            replyMessage(username)
        elif  inp == 'Manage' or inp == 'manage':
            deleteMessage(username)
        elif inp == '0':
            return
        else:
            print("Invalid input, please try again.")


#function to delete a message
def deleteMessage(username):
    message = input("Please copy and paste the message that you would like to delete (only the body): ")
    delete(username, message)
    print("The message has been deleted.")


#check if for deletion priviledges
def delete(username, message):
    file = open("mailboxDataBase.txt", "r")
    lines = file.readlines()
    file.close()

    new_file = open("mailboxDataBase.txt", "w")
    t = message
    r = "TO:: " + username
    for line in lines:
        if r not in line and t not in line:
            new_file.write(line)


#function to reply to an inbox message
def replyMessage(username):
    reply = 'y'
    while reply != 'Y' or reply != 'y' or reply != 'N' or reply != 'n':
        reply = input("\nWould you like to reply to any of these messages? (Y/N): ")
        if reply == 'Y' or reply == 'y':
            sender = input("Please enter the full name of the user you'd like to reply to: ")
            if userinInbox(sender, username):
                sendMessage(sender)
                return
            else:
                print("No conversation found between you and " + sender + ".")
        elif reply == 'N' or reply == 'n':
            return
        else:
            print("Invalid input, please enter Y to reply or N to go back to your mailbox.")


#check if user sent message
def userinInbox(sender, username):
    file = open("mailboxDataBase.txt", "r")
    lines = file.readlines()
    file.close()

    t = "TO:: " + username
    r = "From::" + sender

    for line in lines:
        if line.find(r) != -1 and line.find(t) != -1:
            return True

    return False


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
                    sendMessage(cmd, username)
                    return

        if (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")


#plus members able to message all users
def messageUser(username):
    count = 0
    print("------------------")
    print("|    User List   |")

    nameFile = open("accounts.txt", "r")

    users = nameFile.readlines()

    for line in users:
        if username not in line:
            print(line)
            count = count + 1

    if count == 0:
        print("  No users found")
    print("------------------")

    nameFile.close()

    if count != 0:
        cmd = ""
        while cmd != "0":

            print("")
            print("| '0' to return to main page             |")
            cmd = input("| Enter the name of the user you want to message: ")

            with open('accounts.txt', 'r') as f:
                if cmd in f.read():
                    sendMessage(cmd)
                    return

            if cmd == '0':
                return
            else:
                print("Invalid input, please try again")
                print("")


#check if member is plus or standard
def isPlus(username):
    if "++" not in username:
        return False
    return True

    
def sendMessage(friend, user):
    m = input("Please enter the message you want to send to "+ friend +":")

    file = open("mailboxDataBase.txt", "a")
    file.write("TO:: " +friend + ": "+ m + " From::" + user +"\n")


def registerPlusUser(name):
    
    NewLines =[]
    opn = open("accounts.txt", "r")
    lines = opn.readlines()
    opn.close()
                        
    newName = name + "++"
    for line in lines:
        newline = line.replace(name, newName)
        NewLines.append(newline)
            
    clos = open("accounts.txt", "w+")
    for line in NewLines:
        clos.write(line)
    
    name = name + "++"
    clos.close()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+ Congratulations!! you have registerd as a plus user +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    