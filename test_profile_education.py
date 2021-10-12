#import Users
#from testBase_imporantLinks 
#from TestBase_Important_Links import home, Menu
#
from profile import showProfile
from testBaseEpic4 import addExperience, mainPage, addEducation
from testHelper import mock_input, mock_input_output_end,mock_input_output_start,get_output,set_input
from test_users import set_keyboard_input


#Get to the menu correctly
def test_Profile_Enter():
    mock_input_output_start()
    set_input(["0","5"])
    mainPage('')
    
    output = get_output()

    assert output == [
    "",
        "*************",
        "* InCollege *",
        "*************",
        "",
        "Main page",
        "------------------------------------",
        "| '1' to find someone you know      |",
        "| '2' for learn new skill           |",
        "| '3' for job search/ internship    |",
        "| '4' for useful links              |",
        "| '5' to go to your profile         |",
        "| '0' to return to login            |",
        "-------------------------------------",
        "",
        "Enter page you want to go to: "
        "",
   ]
mock_input_output_end()

def test_Profile_Experience():
    Test = "Student"
    mock_input_output_start()
    set_input(["add","1", "1"])
    addExperience(Test)
    
    output = get_output()

    assert output == [
    'Would you like to add or replace experience?(add/replace) or enter 0 to not '
    'add any experience',
   
    'Invalid input',

   ]
mock_input_output_end()