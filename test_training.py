from testHelper import mock_input_output_end,mock_input_output_start,get_output,set_input
from testBase import messageNotification
import testBase


def test_Training_and_Education():
    mock_input_output_start()

    set_input(["1", "0"])
    TrainingAndEducation()
    output = get_output()

    assert output == [
        '',
        '**************************',
        '* Training and Education *',
        '**************************',
        '',
        'Welcome to Training and Education!',
        '-----------------------------------------------------',
        "| '1' to 'Train for an Interview'                   |",
        "| '2' to 'Learn to Make the Perfect Resume'         |",
        "| '3' to 'Sign Up for InCollege Classes'            |",
        "| '4' to 'Test Your Skills'                         |",
        "| '0' to return to main page                        |",
        '-----------------------------------------------------',
        'What would you like to do: ',
        '',
        '**************************',
        '* Training and Education *',
        '**************************',
        '',
        'Welcome to Training and Education!',
        '-----------------------------------------------------',
        "| '1' to 'Train for an Interview'                   |",
        "| '2' to 'Learn to Make the Perfect Resume'         |",
        "| '3' to 'Sign Up for InCollege Classes'            |",
        "| '4' to 'Test Your Skills'                         |",
        "| '0' to return to main page                        |",
        '-----------------------------------------------------',
        'What would you like to do: ',
        'Invalid input, please try again',
        '']
    mock_input_output_end()


def TrainingAndEducation():
    cmd = ""
    while cmd != '0':
        print("")
        print("**************************")
        print("* Training and Education *")
        print("**************************")
        print("")
        print("Welcome to Training and Education!")
        print("-----------------------------------------------------")
        print("| '1' to 'Train for an Interview'                   |")
        print("| '2' to 'Learn to Make the Perfect Resume'         |")
        print("| '3' to 'Sign Up for InCollege Classes'            |")
        print("| '4' to 'Test Your Skills'                         |")
        print("| '0' to return to main page                        |")
        print("-----------------------------------------------------")
        cmd = input("What would you like to do: ")

    if (cmd == '1'):
        underConstruction()
    elif (cmd == '2'):
        underConstruction()
    elif (cmd == '3'):
        underConstruction()
    elif (cmd == '4'):
        underConstruction()
    else:
        print("Invalid input, please try again")
        print("")

    return

def underConstruction():
    cmd = ""
    while cmd != '0':
        cmd = input("Under Construction...press '0' to return to previous menu.")