from testHelper import mock_input_output_end,mock_input_output_start,get_output,set_input
from testBase import messageNotification
import testBase
import notifications

def test_has_not_create_profile_notification():

    #prep the account
    open('accounts.txt', 'w').close()
    file = open("accounts.txt","a")
    file.write("john++ le\n")
    file.close()

    ret = notifications.createProfileNotification("john++ le")

    assert ret == False

def test_numberOfAppliedJobsNotification():
    mock_input_output_start()
    open('appliedJobs.txt', 'w').close()
    name = "john le"
    title = "job"
    g = "2020"
    s = "2021"
    d = "2022"
    dateApplied = "2024"

    testBase.saveJobApp(name, title, g, s, d, dateApplied)
    notifications.numberOfAppliedJobsNotification(name)
    output = get_output()

    assert output == ["",
                    "NOTIFICATION: You have currently applied for 1 jobs",""]
    mock_input_output_end()

def test_checkLastJobAppliedNotification():
    open('appliedJobs.txt', 'w').close()
    name = "john le"
    title = "job"
    g = "2020"
    s = "2021"
    d = "2022"
    dateApplied = "01/01/2024"
    testDate= "01/20/2024"

    testBase.saveJobApp(name, title, g, s, d, dateApplied)
    #false means more than 7 days? 
    assert testBase.checkLastJobAppliedNotification(name,testDate) == True and testBase.checkLastJobAppliedNotification(name,"01/02/2024") == False

def mainPage(nameofuser):
    global name
    name = nameofuser

    #friend.has_pending_requests(nameofuser)
    
    kbInput = '-1'

    while (kbInput != '0'):
        print("")
        print("*************")
        print("* InCollege *")
        print("*************")
        print("")
        print("Main page")
        print("------------------------------------")
        print("| '1' to find someone you know      |")
        print("| '2' for learn new skill           |")
        print("| '3' for job search/ internship    |")
        print("| '4' for useful links              |")
        print("| '5' to go to your profile         |")
        print("| '6' to show your network          |")
        print("| '7' to show your friendList       |")
        print("| '8' to enter you mailbox          |")
        print("| '0' to return to login            |")
        print("-------------------------------------")
        if "++" not in name:
            print("| '++' to become a PLUS member      |")
            print("-------------------------------------")
        print("")
        notifications.createProfileNotification(nameofuser)
        if messageNotification(name):
            print("You have messages waiting for you.\n")

        if notifications.checkLastJobAppliedNotification(name):
            print("\nRemember – you're going to want to have a job when you graduate."
                  " Make sure that you start to apply for jobs today!\n")

        if notifications.newJobPostedNotification(name):
            print("\nA new job <" +
                  notifications.getTitleForJobNotification(name) + "> has been posted\n")

        if checkNotificationsForNewUser(name):
            print("<" + returnFirstNameOfNewUser(name) +
                  "> <" + returnLastNameOfNewUser(name) +
                  "> x has joined InCollege\n")
            removeNewUserNotification(name)

        kbInput = input("Enter page you want to go to: ")

def removeNewUserNotification(username):
    file = open("newStudentNotification.txt", "r")
    fileRead = file.readlines()
    file.close

    file1 = open("newStudentNotification.txt", "w")

    for line in fileRead:
        if username not in line:
            file1.write(line)


def checkNotificationsForNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            if name == username:
                return True
    return False

#notifies if new job has been posted
def newJobPostedNotification(username):
    file = open("newJobPosted.txt", "r")
    t = username
    for line in file:
        if line != '\n':
            if t in line:
                return True

    return False
           
def getTitleForJobNotification(username):
    file = open("newJobPosted.txt", "r")
    for line in file:
        if line != '\n':
            name, title = line.split('\t')
            if name == username:
                title = title.strip('\n')
                return title

def returnFirstNameOfNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            notifFirstName = notifFirstName.strip('\n')
            if name == username:
                return notifFirstName

def returnFirstNameOfNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            notifFirstName = notifFirstName.strip('\n')
            if name == username:
                return notifFirstName

def returnLastNameOfNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            notifLastName = notifLastName.strip('\n')
            if name == username:
                return notifLastName

def test_NotificationForNewUser():
    nameofuser = "User2"
    mock_input_output_start()
    set_input(["5", "0", "8"])
    mainPage(nameofuser)
    output = get_output()

    assert output == [           '',
            '*************',
           '* InCollege *',
            '*************',
            '',
            'Main page',
            '------------------------------------',
            "| '1' to find someone you know      |",
            "| '2' for learn new skill           |",
            "| '3' for job search/ internship    |",
            "| '4' for useful links              |",
            "| '5' to go to your profile         |",
            "| '6' to show your network          |",
            "| '7' to show your friendList       |",
            "| '8' to enter you mailbox          |",
            "| '0' to return to login            |",
           '-------------------------------------',
              "| '++' to become a PLUS member      |",
           '-------------------------------------',
           '',
            "NOTIFICATION: Don't forget to create a profile!",
       
            'Enter page you want to go to: ',
            '',
            '*************',
            '* InCollege *',
            '*************',
            '',
            'Main page',
            '------------------------------------',
            "| '1' to find someone you know      |",
            "| '2' for learn new skill           |",
            "| '3' for job search/ internship    |",
            "| '4' for useful links              |",
            "| '5' to go to your profile         |",
            "| '6' to show your network          |",
            "| '7' to show your friendList       |",
           "| '8' to enter you mailbox          |",
            "| '0' to return to login            |",
           '-------------------------------------',
              "| '++' to become a PLUS member      |",
           '-------------------------------------',
            '',
           "NOTIFICATION: Don't forget to create a profile!",
    
            'Enter page you want to go to: ',
                   
         
          
    ]
    mock_input_output_end()

def test_NotificationForNewJob():
    nameofuser = "john++ le"
    mock_input_output_start()
    set_input(["5", "0"])
    mainPage(nameofuser)
    output = get_output()

    assert output == [
                   
         '',
  '*************',
  '* InCollege *',
  '*************',
          '',
  'Main page',
  '------------------------------------',
 "| '1' to find someone you know      |",
  "| '2' for learn new skill           |",
  "| '3' for job search/ internship    |",
  "| '4' for useful links              |",
  "| '5' to go to your profile         |",
  "| '6' to show your network          |",
 "| '7' to show your friendList       |",
  "| '8' to enter you mailbox          |",
  "| '0' to return to login            |",
 '-------------------------------------',
  '',
 "NOTIFICATION: Don't forget to create a profile!",
  'You have messages waiting for you.\n',
  'Enter page you want to go to: ',
  '',
  '*************',
  '* InCollege *',
  '*************',
  '',
 'Main page',
  '------------------------------------',
  "| '1' to find someone you know      |",
  "| '2' for learn new skill           |",
 "| '3' for job search/ internship    |",
  "| '4' for useful links              |",
 "| '5' to go to your profile         |",
  "| '6' to show your network          |",
  "| '7' to show your friendList       |",
 "| '8' to enter you mailbox          |",
  "| '0' to return to login            |",
  '-------------------------------------',
  '',
 "NOTIFICATION: Don't forget to create a profile!",
 'You have messages waiting for you.\n',
 'Enter page you want to go to: ',
          
    ]
    mock_input_output_end()

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





    
    
