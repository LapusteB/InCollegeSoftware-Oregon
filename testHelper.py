import builtins
import sys 
sys.path.append('')


input_values = []
print_values = []

previous_input = None
previous_print = None


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values, previous_input, previous_print

    input_values = []
    print_values = []

    previous_input = builtins.input
    previous_print = builtins.print

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def mock_input_output_end():
    builtins.input = previous_input
    builtins.print = previous_print


def get_output():
    global print_values
    return print_values


def set_input(mocked_inputs):
    global input_values
    input_values = mocked_inputs