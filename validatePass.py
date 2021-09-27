# regex library
import re


##use to validate pass in create account
## email format:
## minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character


# return true if meets requirement else false
def validatePass(input):
    regex = '^(?=.{8,12}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)'

    # return none if not match
    obj = re.match(regex, input)

    if (obj != None):
        return True
    else:
        return False
