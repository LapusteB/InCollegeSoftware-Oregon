#import Users
from testBaseEpic3 import home, helpCenter, generalPage,menu,businessSolution
#from usefulLinks import menu
from testHelper import mock_input, mock_input_output_end,mock_input_output_start,get_output,set_input

#mock start 
#set input 
#call function 
#get output 
#assert 
#mock end

#test useful links
#from menus 
def test_useful_links_generalPage():
    mock_input_output_start()
    set_input(["0","3","1","0"])
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
                "","---------------------","|    Useful Links   |","---------------------","","These links are provided by InCollege with your future in mind.",
                "Please choose from the following.","-----------------------------------------","| Press '1' for the General page.       |","| Press '2' to Browse InCollege.        |",
                "| Press '3' for Business Solutions.     |","| Press '4' for Directories.            |","| Press '0' to return to previous menu. |","-----------------------------------------",
                "","What would you like to do?: ",
                
                "","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ",""]

    mock_input_output_end()


def test_browse_InCollege_inside_menu():

    mock_input_output_start()
    set_input(["2","0"])
    menu()
    output = get_output()

    assert output == ["","---------------------","|    Useful Links   |","---------------------","","These links are provided by InCollege with your future in mind.",
                "Please choose from the following.","-----------------------------------------","| Press '1' for the General page.       |","| Press '2' to Browse InCollege.        |",
                "| Press '3' for Business Solutions.     |","| Press '4' for Directories.            |","| Press '0' to return to previous menu. |","-----------------------------------------",
                "","What would you like to do?: ","","Page under construction.","","Press '0' to return to previous page: "]
    mock_input_output_end()

def test_selects_business_solution():
    

    mock_input_output_start()
    set_input(["3","0"])
    menu()
    output = get_output()
    assert output == ["","---------------------","|    Useful Links   |","---------------------","","These links are provided by InCollege with your future in mind.",
                "Please choose from the following.","-----------------------------------------","| Press '1' for the General page.       |","| Press '2' to Browse InCollege.        |",
                "| Press '3' for Business Solutions.     |","| Press '4' for Directories.            |","| Press '0' to return to previous menu. |","-----------------------------------------",
                "","What would you like to do?: ",
                "","Page under construction.","","Press '0' to return to previous page: "



                ]

    mock_input_output_end()


def test_selects_directory():
    mock_input_output_start()
    set_input(["4","0"])
    menu()
    output = get_output()
    assert output == ["","---------------------","|    Useful Links   |","---------------------","","These links are provided by InCollege with your future in mind.",
                "Please choose from the following.","-----------------------------------------","| Press '1' for the General page.       |","| Press '2' to Browse InCollege.        |",
                "| Press '3' for Business Solutions.     |","| Press '4' for Directories.            |","| Press '0' to return to previous menu. |","-----------------------------------------",
                "","What would you like to do?: ",
                "","Page under construction.","","Press '0' to return to previous page: "



                ]
def test_selects_directory():
    mock_input_output_start()
    set_input(["4","0"])
    menu()
    output = get_output()
    assert output == ["","---------------------","|    Useful Links   |","---------------------","","These links are provided by InCollege with your future in mind.",
                "Please choose from the following.","-----------------------------------------","| Press '1' for the General page.       |","| Press '2' to Browse InCollege.        |",
                "| Press '3' for Business Solutions.     |","| Press '4' for Directories.            |","| Press '0' to return to previous menu. |","-----------------------------------------",
                "","What would you like to do?: ",
                "","Page under construction.","","Press '0' to return to previous page: "



                ]


#from general 
def test_select_helpCenter():
    mock_input_output_start()
    set_input(["2","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ",
                "","We're here to help!","","Press '0' to return to previous page: "]

def test_sign_up():
    mock_input_output_start()
    set_input(["1","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ","register"]

def test_about_page():
    mock_input_output_start()
    set_input(["3","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ",

                "","In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide",
                "","Press '0' to return to previous page: "]

def test_press_page():
    mock_input_output_start()
    set_input(["4","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ",

                "","In College Pressroom: Stay on top of the latest news, updates, and reports","","Press '0' to return to previous page: "]


def test_blog_page():
    mock_input_output_start()
    set_input(["5","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ","",

                "","Page under construction.","", "Press '0' to return to previous page: "]

def test_careers_page():
    mock_input_output_start()
    set_input(["6","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ",

                "","Page under construction.","", "Press '0' to return to previous page: ",""]

def test_Developers_page():
    mock_input_output_start()
    set_input(["7","0"])
    generalPage()
    output = get_output()
    assert output == ["","-----------------","|    General    |","-----------------","","Use the provided links for general information and commonly accessed pages.",
                "Please choose from the following.","-----------------------------------------","| Press '1' to go to Sign Up.           |","| Press '2' to go to the Help Center.   |",
                "| Press '3' to go to About.             |", "| Press '4' to go to Press.             |", "| Press '5' to go to Blog.              |",
                "| Press '6' to go to Careers.           |","| Press '7' to go to Developers.        |","| Press '0' to return to previous menu. |",
                "-----------------------------------------","","What would you like to do?: ",

                "","Page under construction.","", "Press '0' to return to previous page: "]



            




