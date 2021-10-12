
import builtins
from testBase import login,mainPage,peopleSearchPage, skillsPage,jobSearchPage,register,contacts,play_video
#,register, contacts


#home 
input_values = []
print_values = []

def test_login_back_to_home():
    set_keyboard_input(["0"])

    login('')
    output = get_display_output()
    assert output == ["--------------------------","InCollege Login",
                    "--------------------------","(Press '0' to return)","Username:",
                    ""]


def test_mainPage_back_to_login():
    set_keyboard_input(["6","0"])
    mainPage()
    output = get_display_output()
    assert output == ["","--------------------------------------------------------",
                    "InCollege","--------------------------------------------------------",
                    "Main page"," Enter page you want to go to: ","   '1' to find someone you know, '2' for learn new skills, '3' for search for job, '4' to post a new job, '0' to return to login\n",
                    "Please enter an available option!!\n",
                    
                    "","--------------------------------------------------------",
                    "InCollege","--------------------------------------------------------",
                    "Main page"," Enter page you want to go to: ","   '1' to find someone you know, '2' for learn new skills, '3' for search for job, '4' to post a new job, '0' to return to login\n",""]
    

def test_searchPeople_back_to_mainPage():
    set_keyboard_input(["0","0","0"])
    peopleSearchPage()
    output = get_display_output()
    assert output == ["----------------------------"," Welcome to Contact Search! ",
    "----------------------------","Enter the first name of the contact you're looking for: ",
    "Enter the last name of the contact you're looking for: ","",
    "They are not a part of the InCollege system" + "\n","Press '0' to return.",
    ""]


def test_skillsPage_backTo_mainPage():
    set_keyboard_input(["b"])
    skillsPage()
    output = get_display_output()
    assert output == ["--------------------------------------------------------"
    , "Available skills to learn:", "Enter the Coressponding Number with a skill to learn it today:",
       " 1. LeaderShip",  " 2. Basic programming in Python", " 3. Make an outstanding resume", 
       " 4. Professional writing"," 5. Microsoft Excel basics", " Or enter b for return to mainPage\n"
       , ""
       ]


def test_jobSearch_backTo_mainPage():
    set_keyboard_input(["0","sadfsaf"])
    jobSearchPage()
    output = get_display_output()
    assert output == ["Page under construction.","Press '0' to return.",
                     ""]

def test_register_back_to_home():
    set_keyboard_input(["0"])
    register()
    output = get_display_output()
    assert output == ["-----------------------------","Welcome to the InCollege App!",
                    "-----------------------------","(Press '0' to return)",
                    "Please enter a unique username: ","",
                    ]

def test_contact_back_to_home():
    set_keyboard_input(["0","0","0","0"])
    contacts()
    output = get_display_output()
    assert output == ["----------------------------"," Welcome to Contact Search! ","----------------------------",
                    "Enter the first name of the contact you're looking for: ","Enter the last name of the contact you're looking for: ",
                    "","They are not a part of the InCollege system","Press '0' to return to login/register page or '1' to search again.",""
                    ]



def test_play_video_back_to_home():
    set_keyboard_input(["0","sadfsaf"])
    play_video()
    output = get_display_output()
    assert output == ["Video is now playing\n","Press '0' for home.",
                    ""]




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
