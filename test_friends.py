import login
import friend
import builtins

input_values = []
print_values = []


# Test for max users in username file.
# Must manually adjust number of users in file to >= 10 before test.
def test_has_max_users():
    assert login.has_max_users()


# Test for less <5 users in username file
# Must manually adjust number of users in file to < 10 before test.
def test_has_not_max_users():
    assert login.has_max_users() == False


def test_student_search_lastname():
    set_keyboard_input(["2", "lastname", "Learner2", "y", "n", "0"])
    friend.friendMenu("Student Learner")

    requestFile = open("friend_requested.txt", "r")
    insertSuccess = False
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            if u == "Student Learner":
                if fu == "Student2 Learner2\n":
                    insertSuccess = True
                    break
    requestFile.close()

    assert insertSuccess


def test_student_search_university():
    set_keyboard_input(["2", "university", "U", "y", "n", "0"])
    friend.friendMenu("Student Learner")

    requestFile = open("friend_requested.txt", "r")
    insertSuccess = False
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            if u == "Student Learner":
                if fu == "Student2 Learner2\n":
                    insertSuccess = True
                    break
    requestFile.close()

    assert insertSuccess


def test_student_search_major():
    set_keyboard_input(["2", "major", "M", "y", "n", "0"])
    friend.friendMenu("Student Learner")

    requestFile = open("friend_requested.txt", "r")
    insertSuccess = False
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            if u == "Student Learner":
                if fu == "Student2 Learner2\n":
                    insertSuccess = True
                    break
    requestFile.close()

    assert insertSuccess


# def test_pending_friend_request():
#     set_keyboard_input(["0"])
#     friend.friendMenu("Student Learner")
#
#     requestFile = open("friend_requested.txt", "r")
#     insertSuccess = False
#     for line in requestFile:
#         if line != '\n':
#             u, fu = line.split('\t')
#             if u == "Student Learner":
#                 if fu == "Student2 Learner2\n":
#                     insertSuccess = True
#                     break
#     requestFile.close()
#
#     assert insertSuccess


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
