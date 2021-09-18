from Users import home
import builtins

input_values = []
print_values = []


def test_register():
    set_keyboard_input(["register", "Tester"])
    home("")
    output = get_display_output()
    assert output == ["Please type either: 'Login' or 'Register",
                      "What would you like to do: "
                      "-----------------------------",
                      "Welcome to the InCollege App!",
                      "-----------------------------",
                      "Please enter a unique username: ",
                      "Error, Username already created! Returning home"]


def test_login_correct():
    set_keyboard_input(["login", "Tester", "Feg4%6&ff", "3"])
    home('')
    output = get_display_output()
    assert output == ["Please type either: 'Login' or 'Register",
                      "What would you like to do: ",
                      "--------------------------",
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

def test_login_incorrect_username():
    set_keyboard_input(["login", "incorrect", "Tester", "Feg4%6&ff", "3"])
    home('')
    output = get_display_output()
    assert output == ["Please type either: 'Login' or 'Register",
                      "What would you like to do: ",
                      "--------------------------",
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


def test_login_incorrect_password():
    set_keyboard_input(["login", "Tester", "52FG3f%^dd", "Feg4%6&ff", "3"])
    home('')
    output = get_display_output()
    assert output == ["Please type either: 'Login' or 'Register",
                      "What would you like to do: ",
                      "--------------------------",
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
