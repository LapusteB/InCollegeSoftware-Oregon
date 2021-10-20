import builtins
import views

input_values = []
print_values = []


def test_has_max_jobs():
    un = open("jobs.txt", "r").readlines()
    file = open("jobs.txt", "w")

    isTrue = False

    for i in range(1,11):
        file.write("${i}\n")
    file.close()
    isTrue = views.has_max_jobs()

    file1 = open("jobs.txt", "w")
    for line in un:
        file1.write(line)
    file1.close()

    assert isTrue


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