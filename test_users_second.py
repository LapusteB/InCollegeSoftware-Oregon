from validatePass import validatePass
from login import find_contacts, play_story, play_video, register, username_exists
import builtins
import random
from unittest import mock
import sys

input_values = []
print_values = []

def test_create_account():
    valid_fakeusers = [
         {"username": "newUser46", "password": "abcdefG1!"},
         {"username": "newUser47", "password": "hoanGngu@12"}
    ]

    for user in valid_fakeusers:
        username_valid = username_exists(user["username"])
        password_valid = validatePass(user["password"])
        assert username_valid == False
        assert password_valid == True

def test_video():
    set_keyboard_input(["1"])
    play_video()
    output = get_display_output()
    assert output == ["Video is now playing\n", "Press '0' for home."]

def test_story():
    print_values.clear()
    random.seed(1)
    play_story()
    output = get_display_output()
    assert output == ["John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n'I loved computers. I taught myself to program in high school,\nand thought I was pretty good at it (Apple Basic and 6502 assembler)\nby the time I graduated. I got a job typesetting at a newspaper,\nand enrolled in university part time, taking programming classes.'\n"]


def test_contacts():
    contacts_found = find_contacts("Example Username")
    assert contacts_found == True


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