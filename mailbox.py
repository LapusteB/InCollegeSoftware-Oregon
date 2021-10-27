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
            print("...")
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")
