import login
import builtins

input_values = []
print_values = []


# Tests login with correct input
def test_login_correct():
    set_keyboard_input(["Tester", "Feg4%6&ff", "3"])
    login.login()
    output = get_display_output()
    assert output == ["--------------------------",
                      "InCollege Login",
                      "--------------------------",
                      "Username: ",
                      "Password: ",
                      '',
                      "--------------------------------------------------------",
                      "InCollege",
                      "--------------------------------------------------------",
                      "Main page",
                      " Enter page you want to go to: ",
                      "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
                      '',
                      "--------------------------------------------------------",
                      "Page under construction"]


# Tests login with incorrect username
def test_login_incorrect_username():
    set_keyboard_input(["incorrect", "Tester", "Feg4%6&ff", "3"])
    login.login()
    output = get_display_output()
    assert output == ["--------------------------",
                      "InCollege Login",
                      "--------------------------",
                      "Username: ",
                      "Error, Username is not recognized",
                      "Enter username: ",
                      "Password: ",
                      '',
                      "--------------------------------------------------------",
                      "InCollege",
                      "--------------------------------------------------------",
                      "Main page",
                      " Enter page you want to go to: ",
                      "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
                      '',
                      "--------------------------------------------------------",
                      "Page under construction"]


# Tests login with incorrect password
def test_login_incorrect_password():
    set_keyboard_input(["Tester", "52FG3f%^dd", "Feg4%6&ff", "3"])
    login.login()
    output = get_display_output()
    assert output == ["--------------------------",
                      "InCollege Login",
                      "--------------------------",
                      "Username: ",
                      "Password: ",
                      "Error, Incorrect password",
                      "Enter password: ",
                      '',
                      "--------------------------------------------------------",
                      "InCollege",
                      "--------------------------------------------------------",
                      "Main page",
                      " Enter page you want to go to: ",
                      "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
                      '',
                      "--------------------------------------------------------",
                      "Page under construction"]


# Test for max users in username file.
# Must manually adjust number of users in file to >= 5 before test.
def test_has_max_users():
    assert login.has_max_users()


# Test for less <5 users in username file
# Must manually adjust number of users in file to < 5 before test.
def test_has_not_max_users():
    assert login.has_max_users() == False


# Tests if username exists in username file.
# Tester is defaulted in this file.
def test_username_exists():
    assert login.username_exists("Tester")


# Tests if username does not exist in username file
# Not Tester cannot be created in username file for testing purposes
def test_username_not_exists():
    assert login.username_exists("Not Tester") == False


# Tests a correct register of a user
# This assumes that there is not already a max amount of users
def test_register():
    set_keyboard_input(["Another Tester", "Abcdefg1!", "3"])
    login.register()
    output = get_display_output()
    assert output == ["-----------------------------",
                      "Welcome to the InCollege App!",
                      "-----------------------------",
                      "Please enter a unique username: ",
                      "Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character",
                      "Please enter a valid password: ",
                      "Account Created!",
                      "Entering main page....",
                      '',
                      "--------------------------------------------------------",
                      "InCollege",
                      "--------------------------------------------------------",
                      "Main page",
                      " Enter page you want to go to: ",
                      "   1 to find someone you know, 2 for learn new skills, 3 for search for job\n",
                      '',
                      "--------------------------------------------------------",
                      "Page under construction"]


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
