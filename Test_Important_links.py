#import Users
#from testBase_imporantLinks 
#from TestBase_Important_Links import home, Menu
from testBaseEpic3 import home, helpCenter, generalPage,Menu,businessSolution
from testHelper import mock_input, mock_input_output_end,mock_input_output_start,get_output,set_input
from test_users import set_keyboard_input


#Get to the menu correctly
def test_important_links_Menu():
    mock_input_output_start()
    set_input(["0","4","a"])
    home('')
    output = get_output()

    assert output == ["\nPlease type either: 'Login' or 'Register'. You can also press 0 for more options.","What would you like to do: ",
                "","--------------------------------------------------------------------------","| Press '1' to find contacts that use InCollege.                         |",
                "| Press '2' to see a video of a successful student who used InCollege!   |",
                "| Press '3' to go to the 'Useful Links' page.                            |",
                "| Press '4' to go to the 'InCollege Important Links' page.               |",
                "| Press '0' to return to the Home menu.                                  |",
                "--------------------------------------------------------------------------"
                ,"What would you like to do: ",
                "\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: "
                , "Invalid input, please try again.\n"]
    mock_input_output_end()

def test_Copyright():
    mock_input_output_start()
    set_input(["1","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "--------------------------",
                "|    Copyright Notice    |",
                "--------------------------",
                "\nCopyright 2021, Team Oregon. All rights reserved.",
                "\nPress '0' to return to previous page: ",]
    mock_input_output_end()

def test_about():
    mock_input_output_start()
    set_input(["2","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide",
                "",
                "Press '0' to return to previous page: ",]
    mock_input_output_end()

def test_Accessibility():
    mock_input_output_start()
    set_input(["3","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "-----------------------",
                "|    Accessibility    |",
                "-----------------------",
                "\nInCollege is accessible in the following ways:",
                "1. Clear headings are used to organize the structure of the content clearly.",
                "2. Text-based so color does not affect the experience of the user.",
                "3. All links have unique and descriptive names for easier navigation.",
                "4. All content can be accessed using the keyboard alone.",
                "5. No dynamic content, making it easy for screen readers to navigate the application.",
                "\nPress '0' to return to previous page: ",]
    mock_input_output_end()


def test_User_Agreement():
    mock_input_output_start()
    set_input(["4","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "------------------------",
   "|    User Agreement    |",
    "------------------------",

    "\nWelcome, and thanks for using InCollege!",
    "Please take a minute and read over the user agreement.",

    "\nThis agreement is a legal contract between you and us.",
    "You acknowledge that you have read and understood the terms of this agreement.",
    "If you do not agree to the terms of this agreement, you should not use InCollege.",
    "We may, at any time, terminate your account or priviledges for violations of this agreement.",

    "\nIntellectual Property",
    "Team Oregon owns all rights, titles, and interest in and to this application.",
    "You may not modify, adapt, translate, decompile, or attempt to retrieve source code from this application.",
    
    "\nPrivacy",
    "We will not use or sell your information to external entities.",
    "When you use InCollege you can be confident that your private information is safe from external attacks.",
    "When you make a post on InCollege, be aware that this is public and it may be seen by other users, or non-users of this application.",
     "\nPress '0' to return to previous page: ",]
    mock_input_output_end()

def test_Privacy_Policy():
    mock_input_output_start()
    set_input(["5","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
               "------------------------",
    "|    Privacy Policy    |",
    "------------------------",
    "\nWhen you use InCollege, you may give us certain information voluntarily.",
    "This includes your name, employer, location, and any other information you give us.",

    "\nWe utilize this information to create a more personalized experience for you, the user.",
    "This information will not be sold or given to any external entities.",
    "\nPlease note that any personal information posted publicly and voluntarily, may be seen by others.",
    "\nPress '0' to return to previous page: ",]
    mock_input_output_end()

def test_Cookie_Policy():
    mock_input_output_start()
    set_input(["6","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "-----------------------",
    "|    Cookie Policy    |",
    "-----------------------",
    "\nThis application does not currently utilize cookies.",
    "\nPress '0' to return to previous page: ",]
    mock_input_output_end()

def test_CopyRight_Policy():
    mock_input_output_start()
    set_input(["7","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "--------------------------",
    "|    Copyright Policy    |",
    "--------------------------",
    "\nWe at Team Oregon recognize and respect intellectual property rights and are committed to ",
    "fulfilling our moral and legal obligations with respect to our use of copyright-protected works.",

    "\nTeam Oregon expects its employees to be responsible when consuming copyrighted materials.",
    "Employees who duplicate copyrighted works may be subject to termination, or other disciplinary actions.",
    "\nPress '0' to return to previous page: "]
    mock_input_output_end()

def test_Brand_Policy():
    mock_input_output_start()
    set_input(["8","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                "Enter the page you want to go to: ",
                "",
                "----------------------",
    "|    Brand Policy    |",
    "----------------------",
    "\nEntities may only use InCollege trademarks in strict accordance with this policy.",
    
    "\nNo entity may alter or combine InCollege trademarks with any other elements.",
    "The use of InCollege icons, graphics, or logos without direct permission from Team Oregon, is not allowed.",
    "The use of InCollege trademarks for commercial merchandise is prohibited.",
    "\nPress '0' to return to previous page: "]
    mock_input_output_end()

def test_Guest_Controls():
    mock_input_output_start()
    set_input(["9","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                 "Enter the page you want to go to: ",
               "",
                "------------------------",
    "|    Guest Controls    |",
    "------------------------",
    "\nYour current preferences are: ",
    "Email: on\n",
    "SMS: on\n",
    "Targeted Advertising: on",
    "Press '0' to return to previous page or '1' to edit your preferences: "]
    mock_input_output_end()

def test_Languages():
    mock_input_output_start()
    set_input(["10","0"])
    Menu()
    output = get_output()

    assert output == ["\n------------------------",
                "| Important Links Menu |",
                "------------------------\n",
                "Please choose from the following.\n",
                "-------------------------------------------",
                "| Press '1' for the Copyright Notice.     |",
                "| Press '2' for About.                    |",
                "| Press '3' for Accessibility.            |",
                "| Press '4' for the User Agreement.       |",
                "| Press '5' for the Privacy Policy.       |",
                "| Press '6' for the Cookie Policy.        |",
                "| Press '7' for the Copyright Policy.     |",
                "| Press '8' for the Brand Policy.         |",
                "| Press '9' for the Guest Controls.       |",
                "| Press '10' for Languages.               |",
                "| Press '0' to return to previous menu.   |",
                "-------------------------------------------",
                 "Enter the page you want to go to: ",
                 "",
                  "-------------------",
    "|    Languages    |",
    "-------------------",
 'Welcome, your current application language is English.\n',
"Select '2' to change language to Spanish, or '0' to quit: ",
              ]
    mock_input_output_end()

