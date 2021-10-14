import login
import friend
import builtins

input_values = []
print_values = []


def test_has_max_users():
    un = open("usernames.txt", "r").readlines()
    file = open("usernames.txt", "w")

    isTrue = False

    for i in range(1,11):
        file.write("${i}\n")
    file.close()
    isTrue = login.has_max_users()

    file1 = open("usernames.txt", "w")
    for line in un:
        file1.write(line)
    file1.close()

    assert isTrue


def test_has_not_max_users():
    un = open("usernames.txt", "r").readlines()
    file = open("usernames.txt", "w")

    isTrue = False

    for i in range(1,5):
        file.write("${i}\n")
    file.close()
    isTrue = login.has_max_users()

    file1 = open("usernames.txt", "w")
    for line in un:
        file1.write(line)
    file1.close()

    assert isTrue == False


def test_student_search_lastname():
    friendRequests = open("friend_requested.txt", "r").readlines()
    fr = open("friendList.txt", "w")
    fr.close()

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

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequests:
        fr1.write(request)
    fr1.close()

    assert insertSuccess


def test_student_search_university():
    friendRequests = open("friend_requested.txt", "r").readlines()
    fr = open("friendList.txt", "w")
    fr.close()

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

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequests:
        fr1.write(request)
    fr1.close()

    assert insertSuccess


def test_student_search_major():
    friendRequests = open("friend_requested.txt", "r").readlines()
    fr = open("friendList.txt", "w")
    fr.close()

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

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequests:
        fr1.write(request)
    fr1.close()

    assert insertSuccess


def test_show_network_fl_fill():
    friendList = open("friendList.txt", "r").readlines()
    friendRequest = open("friend_requested.txt", "r").readlines()

    fr = open("friend_requested.txt", "w")
    fr.close()

    fl = open("friendList.txt", "w")
    fl.write("Student Learner\tStudent2 Learner2\n")
    fl.close()

    set_keyboard_input(["0"])
    friend.friendMenu("Student Learner")
    output = get_display_output()

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequest:
        fr1.write(request)
    fr1.close()

    fl1 = open("friendList.txt", "w")
    for friends in friendList:
        fl1.write(friends)
    fl1.close()

    assert output == ["Your pending friend requests:\n",
                      "No pending friend requests",
                      "Your friends:\n",
                      "Friend username: Student2 Learner2\n",
                      "",
                      "------------------------------------------",
                      "| '1' to show your network               |",
                      "| '2' to search people and send request  |",
                      "| '3' to disconnect network              |",
                      "| '0' to return to main page             |",
                      "------------------------------------------",
                      "What would you like to do: "]


def test_show_network_fr_fill():
    friendList = open("friendList.txt", "r").readlines()
    friendRequest = open("friend_requested.txt", "r").readlines()

    fl = open("friendList.txt", "w")
    fl.close()

    fr = open("friend_requested.txt", "w")
    fr.write("Student Learner\tStudent2 Learner2\n")
    fr.close()

    set_keyboard_input(["0"])
    friend.friendMenu("Student Learner")
    output = get_display_output()

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequest:
        fr1.write(request)
    fr1.close()

    fl1 = open("friendList.txt", "w")
    for friends in friendList:
        fl1.write(friends)
    fl1.close()

    assert output == ["Your pending friend requests:\n",
                      "Waiting friend reuqest response from: Student2 Learner2\n",
                      "Your friends:\n",
                      "No friend to show",
                      "",
                      "------------------------------------------",
                      "| '1' to show your network               |",
                      "| '2' to search people and send request  |",
                      "| '3' to disconnect network              |",
                      "| '0' to return to main page             |",
                      "------------------------------------------",
                      "What would you like to do: "]


def test_show_network_empty_files():
    friendList = open("friendList.txt", "r").readlines()
    friendRequest = open("friend_requested.txt", "r").readlines()

    fl = open("friendList.txt", "w")
    fl.close()

    fr = open("friend_requested.txt", "w")
    fr.close()

    set_keyboard_input(["0"])
    friend.friendMenu("Student Learner")
    output = get_display_output()

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequest:
        fr1.write(request)
    fr1.close()

    fl1 = open("friendList.txt", "w")
    for friends in friendList:
        fl1.write(friends)
    fl1.close()

    assert output == ["Your pending friend requests:\n",
                      "No pending friend requests",
                      "Your friends:\n",
                      "No friend to show",
                      "",
                      "------------------------------------------",
                      "| '1' to show your network               |",
                      "| '2' to search people and send request  |",
                      "| '3' to disconnect network              |",
                      "| '0' to return to main page             |",
                      "------------------------------------------",
                      "What would you like to do: "]

def test_show_network_filled_files():
    friendList = open("friendList.txt", "r").readlines()
    friendRequest = open("friend_requested.txt", "r").readlines()

    fl = open("friendList.txt", "w")
    fl.write("Student Learner\tStudent2 Learner2\n")
    fl.close()

    fr = open("friend_requested.txt", "w")
    fr.write("Student Learner\tA Tester")
    fr.close()

    set_keyboard_input(["0"])
    friend.friendMenu("Student Learner")
    output = get_display_output()

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequest:
        fr1.write(request)
    fr1.close()

    fl1 = open("friendList.txt", "w")
    for friends in friendList:
        fl1.write(friends)
    fl1.close()

    assert output == ["Your pending friend requests:\n",
                      "Waiting friend reuqest response from: A Tester",
                      "Your friends:\n",
                      "Friend username: Student2 Learner2\n",
                      "",
                      "------------------------------------------",
                      "| '1' to show your network               |",
                      "| '2' to search people and send request  |",
                      "| '3' to disconnect network              |",
                      "| '0' to return to main page             |",
                      "------------------------------------------",
                      "What would you like to do: "]


def test_pending_friend_request():
    friendRequests = open("friend_requested.txt", "r").readlines()
    friendList = open("friendList.txt", "r").readlines()

    fl = open("friend_requested.txt", "w")
    fl.close()
    fr = open("friendList.txt", "w")
    fr.write("Student Learner\tStudent2 Learner2\n")
    fr.close()

    set_keyboard_input(["accept"])
    friend.has_pending_requests("Student2 Learner2")

    requestFile = open("friendList.txt", "r")
    insertSuccess = False
    for line in requestFile:
        if line != '\n':
            u, fu = line.split('\t')
            if u == "Student Learner":
                if fu == "Student2 Learner2\n":
                    insertSuccess = True
                    break
    requestFile.close()

    fr1 = open("friend_requested.txt", "w")
    for request in friendRequests:
        fr1.write(request)
    fr1.close()

    fl1 = open("friendList.txt", "w")
    for friends in friendList:
        fl1.write(friends)
    fl1.close()

    assert insertSuccess


def test_disconnect():
    fl = open("friendList.txt", "r").readlines()

    file = open("friendList.txt", "w")
    file.write("Student2 Learner2\tStudent Learner\n")
    file.close()

    set_keyboard_input(["Student Learner"])
    friend.disconnect_network("Student2 Learner2")

    friendList = open("friendList.txt", "r").readlines()

    file1 = open("friendList.txt", "w")
    for line in fl:
        file1.write(line)
    file1.close()

    assert len(friendList) == 0


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
