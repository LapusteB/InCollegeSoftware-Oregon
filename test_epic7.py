from testHelper import mock_input_output_end,mock_input_output_start,get_output,set_input
import testBase

#accounts.txt
def test_plus_user_send_messsage():
    
    mock_input_output_start()
    set_input(["2","john++ le","The message"])

    #prep the accounts.txt file, (add friend)
    open('accounts.txt', 'w').close()
    file = open("accounts.txt","a")
    file.write("john++ le\n")
    file.close()

    m = "The message"
    user = "van++ le"
    friend = "john++ le"
    message = "TO:: " +friend + ": "+ m + " From::" + user +"\n"

    #call function mailbox
    testBase.mailboxMenu("van++ le")

    output = get_output()

    #make sure it is in there.
    file2 = open("mailboxDataBase.txt")

    #the output and the message:
    assert output == ["----------Welcome to mailbox-------------", "",
        "------------------------------------------",
        "| '1' to open inbox                      |", 
        "| '2' to message a friend                |","| '0' to return to main page             |",
        "------------------------------------------",
        "What would you like to do: ",
        "------------------",
        "|    User List   |","john++ le\n",
        '------------------',
        "", "| '0' to return to main page             |",
        "| Enter the name of the user you want to message: ", 
        "Please enter the message you want to send to "+ friend +":"] and message in file2.read()
    
    file2.close()

    mock_input_output_end()

                
    

