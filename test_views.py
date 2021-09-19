from views import mainPage
import builtins

input_values = []
print_values = []

def test_jobSearch():
    set_keyboard_input(["3"])
    mainPage()
    output = get_display_output()
    assert output == [ "", "--------------------------------------------------------",
        "InCollege","--------------------------------------------------------", "Main page"," Enter page you want to go to: ",
         "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
         "", "--------------------------------------------------------","Page under construction"]

def test_findSomeone():
    set_keyboard_input(["1"])
    mainPage()
    output = get_display_output()
    assert output == [ "", "--------------------------------------------------------",
        "InCollege","--------------------------------------------------------", "Main page"," Enter page you want to go to: ",
         "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
         "", "--------------------------------------------------------","Page under construction"]

def test_learnSkills():
    set_keyboard_input(["2","1"])
    mainPage()
    output = get_display_output()
    assert output == [ "", "--------------------------------------------------------",
        "InCollege","--------------------------------------------------------", "Main page"," Enter page you want to go to: ",
         "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
        "--------------------------------------------------------",
        "Available skills to learn:", 
        "Enter the Coressponding Number with a skill to learn it today:",
        " 1. LeaderShip", " 2. Basic programming in Python",
        " 3. Make an outstanding resume", " 4. Professional writing",
        " 5. Microsoft Excel basics", " Or enter b for return to mainPage\n",
        "", "--------------------------------------------------------","Page under construction"]


def test_learnSkills_main():
    set_keyboard_input(["2","b","1"])
    mainPage()
    output = get_display_output()
    assert output == ["", "--------------------------------------------------------",
        "InCollege","--------------------------------------------------------", "Main page"," Enter page you want to go to: ",
         "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
        "--------------------------------------------------------",
        "Available skills to learn:", 
        "Enter the Coressponding Number with a skill to learn it today:",
        " 1. LeaderShip", " 2. Basic programming in Python",
        " 3. Make an outstanding resume", " 4. Professional writing",
        " 5. Microsoft Excel basics", " Or enter b for return to mainPage\n",
        "", "--------------------------------------------------------",
        "InCollege","--------------------------------------------------------", "Main page"," Enter page you want to go to: ",
         "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
         "", "--------------------------------------------------------","Page under construction"]

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