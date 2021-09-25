
import builtins
from Users import login,register, contacts
from views import mainPage, peopleSearchPage, skillsPage, jobSearchPage,postNewJob


#home 
input_values = []
print_values = []

def test_login_back_to_home():
    set_keyboard_input(["0","terminate"])

    login('')
    output = get_display_output()
    assert output == ["--------------------------","InCollege Login",
                    "--------------------------","(Press '0' to return)",
                    "Username:","John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n" +
    "'I loved computers. I taught myself to program in high school,\n" +
    "and thought I was pretty good at it (Apple Basic and 6502 assembler)\n" +
    "by the time I graduated. I got a job typesetting at a newspaper,\n" +
    "and enrolled in university part time, taking programming classes.'\n","\nPlease type either: 'Login' or 'Register'. You can also press '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!",
    "What would you like to do: "]


def test_mainPage_back_to_login():
    set_keyboard_input(["0","sadfsaf"])
    mainPage()
    output = get_display_output()
    assert output == ["","--------------------------------------------------------",
                    "InCollege","--------------------------------------------------------",
                    "Main page","   '1' to find someone you know, '2' for learn new skills, '3' for search for job, '4' to post a new job, '0' to return to login\n",
                    "John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n" +
    "'I loved computers. I taught myself to program in high school,\n" +
    "and thought I was pretty good at it (Apple Basic and 6502 assembler)\n" +
    "by the time I graduated. I got a job typesetting at a newspaper,\n" +
    "and enrolled in university part time, taking programming classes.'\n","\nPlease type either: 'Login' or 'Register'. You can also press '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!",
    "What would you like to do: "]
    

def test_searchPeople_back_to_mainPage():
    set_keyboard_input(["0","sadfsaf"])
    peopleSearchPage()
    output = get_display_output()
    assert output == ["----------------------------"," Welcome to Contact Search! ",
    "----------------------------","Enter the first name of the contact you're looking for: ",
    "Enter the last name of the contact you're looking for: ","",
    "They are not a part of the InCollege system" + "\n","Press '0' to return.",

    "","--------------------------------------------------------","InCollege",
    "Main page"," Enter page you want to go to: "]

def test_skillsPage_backTo_mainPage():
    set_keyboard_input(["b","sadfsaf"])
    skillsPage()
    output = get_display_output()
    assert output == ["--------------------------------------------------------"
    , "Available skills to learn:", "Enter the Coressponding Number with a skill to learn it today:",
       " 1. LeaderShip",  " 2. Basic programming in Python", " 3. Make an outstanding resume", 
       " 4. Professional writing"," 5. Microsoft Excel basics", " Or enter b for return to mainPage\n"
       , 
       "","--------------------------------------------------------","InCollege",
    "Main page"," Enter page you want to go to: "
       ]

def test_jobSearch_backTo_mainPage():
    set_keyboard_input(["0","sadfsaf"])
    jobSearchPage()
    output = get_display_output()
    assert output == ["Page under construction.","Press '0' to return.",
                     "","--------------------------------------------------------","InCollege",
    "Main page"," Enter page you want to go to: "]

def test_register_back_to_home():
    set_keyboard_input(["0","0"])
    register()
    output = get_display_output()
    assert output == ["-----------------------------","Welcome to the InCollege App!",
                    "-----------------------------","(Press '0' to return)",
                    "Please enter a unique username: ",
                    "John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n" +
    "'I loved computers. I taught myself to program in high school,\n" +
    "and thought I was pretty good at it (Apple Basic and 6502 assembler)\n" +
    "by the time I graduated. I got a job typesetting at a newspaper,\n" +
    "and enrolled in university part time, taking programming classes.'\n","\nPlease type either: 'Login' or 'Register'. You can also press '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!",
    "What would you like to do: "]

def test_contact_back_to_home():
    set_keyboard_input(["0","0","0","0"])
    contacts()
    output = get_display_output()
    assert output == ["----------------------------"," Welcome to Contact Search! ","----------------------------",
                    "Enter the first name of the contact you're looking for: ","Enter the last name of the contact you're looking for: ",
                    "","They are not a part of the InCollege system",
                     "John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n" +
    "'I loved computers. I taught myself to program in high school,\n" +
    "and thought I was pretty good at it (Apple Basic and 6502 assembler)\n" +
    "by the time I graduated. I got a job typesetting at a newspaper,\n" +
    "and enrolled in university part time, taking programming classes.'\n","\nPlease type either: 'Login' or 'Register'. You can also press '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!",
    "What would you like to do: "]



def test_video_back_to_home():
    set_keyboard_input(["0","sadfsaf"])
    mainPage()
    output = get_display_output()
    assert output == ["Video is now playing\n","Press '0' for home.",
                    "John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n" +
    "'I loved computers. I taught myself to program in high school,\n" +
    "and thought I was pretty good at it (Apple Basic and 6502 assembler)\n" +
    "by the time I graduated. I got a job typesetting at a newspaper,\n" +
    "and enrolled in university part time, taking programming classes.'\n","\nPlease type either: 'Login' or 'Register'. You can also press '0' to find contacts that use InCollege or press '1' to see a video of a sucessful student who used InCollege!",
    "What would you like to do: "]



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
