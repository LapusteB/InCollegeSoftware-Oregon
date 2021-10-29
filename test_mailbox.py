import mailbox
import builtins
import testBaseEpic7

input_values = []
print_values = []


def testStandardMessageNotFriend():
    friendFile=open("friendList.txt", "w")
    friendFile.write("Student Learner\tStudent Learner2\n")
    friendFile.close()
    
    set_keyboard_input(["Student3 Learner3", "This is testing"])

    mailbox.messageFriend("Student Learner")

    maildbFile = open("mailboxDataBase.txt", "r")
    maildbline = maildbFile.readlines()
    maildbFile.close()
    found = False
    for line in maildbline:
        if line != '\n':
            if str("TO:: Student3 Learner3: This is testing From::Student Learner\n") in line:
                found = True

    assert found == False

def testStandardMessageFriend():
    friendFile=open("friendList.txt", "w")
    friendFile.write("Student Learner\tStudent Learner2\n")
    friendFile.close()
    
    set_keyboard_input(["Student2 Learner2", "This is testing"])

    testBaseEpic7.messageFriend("Student Learner")

    maildbFile = open("mailboxDataBase.txt", "r")
    maildbline = maildbFile.readlines()
    maildbFile.close()
    found = False
    for line in maildbline:
        if line != '\n':
            if str("TO:: Student2 Learner2: This is testing From::Student Learner\n") in line:
                found = True

    assert found == True

def testChoicePlus():
    testBaseEpic7.registerPlusUser("Student Learner")

    accountFile = open("accounts.txt", "r")
    accountline = accountFile.readlines()
    accountFile.close()
    found = False
    for line in accountline:
        if line != '\n':
            if str("Student Learner++") in line:
                found = True

    assert found == True

def testinbox():
    set_keyboard_input(["This is testing"])

    testBaseEpic7.sendMessage("Student Learner", "Student2 Learner2")

    testBaseEpic7.inbox("Student Learner")

    output = get_display_output()

    assert output == ["Please enter the message you want to send to Student Learner:"
        ,['TO:: Student Learner: This is testing From::Student2 Learner2\n']]

def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)

def mock_input_output_start():
    global input_values, print_values
    input_values = []
    print_values = []
    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)

def get_display_output():
    global print_values
    return print_values

def set_keyboard_input(mocked_inputs):
    global input_values
    mock_input_output_start()
    input_values = mocked_inputs