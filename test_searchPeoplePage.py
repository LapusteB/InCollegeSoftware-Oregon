
from testBase import mock_input_output_start, mock_input_output_end, set_input, get_output

input_values = []
print_values = []


def find_contacts(n):
    with open('accounts.txt') as f:
        if n in f.read():
            return True
        return False


def peopleSearchPage():
    a = -1
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    file3 = open("accounts.txt", "r")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname

    if (find_contacts(name)):
        print("")
        print("They are a part of the InCollege system." + "\n")
        #mainPage()
    else:
        print("")
        print("They are not a part of the InCollege system" + "\n")
        #mainPage()
    a = input("Press '0' to return.")
    if int(a) == 0:
        #mainPage()
        print("quit")

    file3.close()

def test_search_people_in_system():
    mock_input_output_start()
    set_input(["van","le",0])
    peopleSearchPage()
    output = get_output()
    assert output == ["----------------------------"," Welcome to Contact Search! ",
                    "----------------------------","Enter the first name of the contact you're looking for: ",
                    "Enter the last name of the contact you're looking for: ","",
                    "They are a part of the InCollege system." + "\n","Press '0' to return.","quit"]
    mock_input_output_end()


def test_search_people_not_in_system():
    mock_input_output_start()
    set_input(["asdf","asdf","0"])
    peopleSearchPage()
    output = get_output()
    assert output == ["----------------------------"," Welcome to Contact Search! ",
                    "----------------------------","Enter the first name of the contact you're looking for: ",
                    "Enter the last name of the contact you're looking for: ","",
                    "They are not a part of the InCollege system" + "\n","Press '0' to return.","quit"]
                    