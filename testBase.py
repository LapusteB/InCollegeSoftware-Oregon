import builtins
from validatePass import validatePass



def has_max_users():
    count = 0
    for line in open("usernames.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted accounts have been created, please come backlater")
        return True
    return False
def username_exists(u):
    with open('usernames.txt') as f:
        if u in f.read():
            return True
        return False
def play_video():
    print("Video is now playing\n")
    a = input("Press '0' for home." )
    if(int(a) == 0):
        print("")
        #home('')


input_values = []
print_values = []

previous_input = None
previous_print = None


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values, previous_input, previous_print

    input_values = []
    print_values = []

    previous_input = builtins.input
    previous_print = builtins.print

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def mock_input_output_end():
    builtins.input = previous_input
    builtins.print = previous_print


def get_output():
    global print_values
    return print_values


def set_input(mocked_inputs):
    global input_values
    input_values = mocked_inputs

def contacts():
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    file3 = open("accounts.txt", "r")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname

    if (find_contacts(name)):
        print("")
        print("They are a part of the InCollege system. Register or login now to join them!" + "\n")
        print("")
        #home('')
    else:
        print("")
        print("They are not a part of the InCollege system")
        no_contacts = input("Press '0' to return to login/register page or '1' to search again.")
        if (int(no_contacts) == 0):
            print("")
            #home('')
        elif (int(no_contacts) == 1):
            contacts()

def max_job():
    print("max jobs 5")

def postNewJob():
    select = "x"
    print("-----------------------------------")
    print(" Welcome to the Job Creation Page! ")
    print("-----------------------------------")
    while(select != 'y' and select != 'Y' and select != 'n' and select != "N"):
        select = input("Would you like to create a job? ('y' or 'n'): ")
        if (select == 'y' or select =='Y'):
            if (has_max_jobs()):
                max_job()
            createNewJob()
        elif (select == 'n' or select == 'N'):
            #mainPage()
            print("")
        else:
            print("Invalid input please try again.")



def has_max_jobs():
    count = 0
    for line in open("jobs.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted jobs have been posted, please come back later." + "\n")
        return True
    return False




def createNewJob():
    print("")
    title = input("Enter the title for your job: ")
    description = input("Enter the description for your job: ")
    employer = input("Enter the employer for your job: ")
    location = input("Enter the location for your job: ")
    salary = input("Enter the salary for your job: ")

    saveJob(title, description, employer, location, salary)


def saveJob(t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()

def home(user):
    #play_story()
    print("\nPlease type either: 'Login' or 'Register'. You can also press '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!")
    a = input("What would you like to do: ")
    if (a == "register" or a == "Register"):
        #register()
        print("")
    elif (a == "Login" or a == "login"):
        login(user)
        print("")
    elif(int(a) == 1):
        #play_video()
        print("")
        
    elif(int(a) == 0):
        #contacts()
        print("")
    else:
        print("Choose a valid option")
        home('')


def login(user):
    print("--------------------------")
    print("InCollege Login")
    print("--------------------------")
    file = open("usernames.txt", "a")
    file2 = open("passwords.txt", "a")
    indexU = 0
    

    filename = "usernames.txt"
    with open(filename) as file:
        linesU = file.readlines()
        linesU = [line.rstrip() for line in linesU]

    filename = "passwords.txt"
    with open(filename) as file:
        linesP = file.readlines()
        linesP = [line.rstrip() for line in linesP]

        print("(Press '0' to return)")
    u = input("Username:")
    with open('usernames.txt') as f:
        if u in f.read():
            indexU = linesU.index(u)
            #User.username = u
            u = True
        elif u == "0":
            #home('')
            print("")
        else:
            flag = False
            while flag == False:
                with open('usernames.txt') as f:
                    if u in f.read():
                        indexU = linesU.index(u)
                        break
                    else:
                        print("Error, Username is not recognized")
                        x = input("Enter username: ")
                        with open('usernames.txt') as f:
                            if x in f.read():
                                indexU = linesU.index(u)
                                flag = True
                                break
                            else:
                                flag = False
    file.close()
    file2.close()

'''
    p = input("Password: ")
    #flag = validatePass(p)

    
    if p == linesP[indexU]:
        #mainPage()
        print("")
    else:
        while p != linesP[indexU]:
            print("Error, Incorrect password")
            p = input("Enter password: ")
            if p == linesP[indexU]:
                break
        #mainPage()
        print("")
'''
def find_contacts(n):
    with open('accounts.txt') as f:
        if n in f.read():
            return True
        return False

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
                print("")
                #mainPage()       
    

    if(kbInput == "b"):
        print("")
        #mainPage()

def jobSearchPage():
    print("Page under construction.")
    a = input("Press '0' to return.")
    if int(a) == 0:
        print("")
        #mainPage()

def peopleSearchPage():
    a = -1
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    file3 = open("accounts.txt", "r")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname

    if (find_contacts(name)):
        print("")
        print("They are a part of the InCollege system." + "\n")
        #mainPage()
    else:
        print("")
        print("They are not a part of the InCollege system" + "\n")
        #mainPage()
    a = input("Press '0' to return.")
    if int(a) == 0:
        print("")
        #mainPage()

    file3.close()

def register():
    print("-----------------------------")
    print("Welcome to the InCollege App!")
    print("-----------------------------")
    file = open("usernames.txt", "a")  # - file will be created if not present
    file2 = open("passwords.txt", "a")  # - file will be created if not present
    file3 = open("accounts.txt", "a")
    # Checks if there are already 5 accounts made this way
    if has_max_users():
        home('')

    # Checks if there is a duplicate username
    print("(Press '0' to return)")
    u = input("Please enter a unique username: ")
    if username_exists(u):
        print("Error, Username already created! Returning home")
        home('')

    if u == "0":
        print("")
        #home('')
    '''

    file.write(u + "\n")
    print("Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
    p = input("Please enter a valid password: ")
    res = validatePass(p)

    while res is False:
        if res is False:
            print("Error, Please meet password requirements:")
            print("---------------------------------------------")
            print("-minimum of 8 characters")
            print("-maximum of 12 characters")
            print("-at least one capital letter")
            print("-one digit, one non-alpha character")
            print("---------------------------------------------")
        p = input("Re-enter Password: ")
        res = validatePass(p)
    file2.write(p + "\n")
    Fname = input("What is your first name?: ")
    Lname = input("What is your last name?: ")

    file3.write(Fname + " " + Lname + "\n")

    file.close()
    file2.close()
    file3.close()
   

    print("\nHello, " + Fname)
    print("Account Created!")
    print("Entering main page....")
    mainPage()
'''

def mainPage():

    kbInput = "-1"

    while(kbInput != "1" and kbInput != "2" and kbInput != "3" and kbInput != "4" and kbInput != "0"):
        print("")
        print("--------------------------------------------------------")
        print("InCollege")
        print("--------------------------------------------------------")
        print("Main page")
        print(" Enter page you want to go to: ")
        kbInput = input("   '1' to find someone you know, '2' for learn new skills, '3' for search for job, '4' to post a new job, '0' to return to login\n")
        if(kbInput == "1"):
            #peopleSearchPage()
            print("")
        elif(kbInput == "2"):
            #skillsPage()
            print("")
        elif(kbInput == "3"):
            #jobSearchPage()
            print("")
        elif(kbInput == "4"):
            postNewJob()
        elif(kbInput == "0"):
            #from Users import home
            print("")
            #home('')
        else:
            print("Please enter an available option!!\n")
    


#postNewJob()

'''For epic7'''


def sendMessage(friend,user):
    m = input("Please enter the message you want to send to "+ friend +":")

    file = open("mailboxDataBase.txt", "a")
    file.write("TO:: " +friend + ": "+ m + " From::" + user +"\n")
    file.close()

#check if member is plus or standard
def isPlus(username):
    if "++" not in username:
        return False
    return True

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
                    sendMessage(cmd,username)
                    return

            if cmd == '0':
                return
            else:
                print("Invalid input, please try again")
                print("")


def mailboxMenu(username):
    global user
    user = username
    print("----------Welcome to mailbox-------------")

    cmd = ""
    #while(cmd != "0"):
                
    print("")
    print("------------------------------------------")
    print("| '1' to open inbox                      |")
    print("| '2' to message a friend                |")
    print("| '0' to return to main page             |")
    print("------------------------------------------")
    cmd = input("What would you like to do: ")

    if (cmd == '1'):
        #inbox(username)
        print("")
    elif (cmd == '2'):
        if (isPlus(username)):
            messageUser(username)
            #break
        else:
            #messageFriend((username))
            print("")
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
            return
        elif  inp == 'Manage' or inp == 'manage':
            print("")
            #deleteMessage(username)
        elif inp == '0':
            return
        else:
            print("Invalid input, please try again.")

#function to reply to an inbox message
def replyMessage(username):
    reply = 'y'
    while reply != 'Y' or reply != 'y' or reply != 'N' or reply != 'n':
        reply = input("\nWould you like to reply to any of these messages? (Y/N): ")
        if reply == 'Y' or reply == 'y':
            sender = input("Please enter the full name of the user you'd like to reply to: ")
            if userinInbox(sender, username):
                sendMessage(sender,username)
            else:
                print("No conversation found between you and " + sender + ".")
            return
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

def messageNotification(username):
    nameFile = open("mailboxDataBase.txt", "r")
    new_message = nameFile.readlines()
    nameFile.close()

    t = "TO:: " + username
    f = "*"

    for line in new_message:
        if t in line and f in line:
            return True

    return False

def sendMessage2(friend,user):
    m = input("Please enter the message you want to send to "+ friend +":")

    file = open("mailboxDataBase.txt", "a")
    file.write("TO:: " + friend + ": "+ m + " From::" + user +"*\n")





