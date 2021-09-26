import builtins



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

def max_job():
    print("max jobs 5")

def postNewJob():
    select = "x"
    print("-----------------------------------")
    print(" Welcome to the Job Creation Page! ")
    print("-----------------------------------")
    while(select != 'y' and select != 'Y' and select != 'n' and select != "N"):
        select = input("Would you like to create a job? ('y' or 'n'): ")
        if (select == 'y' or select =='Y'):
            if (has_max_jobs()):
                max_job()
            createNewJob()
        elif (select == 'n' or select == 'N'):
            #mainPage()
            print("")
        else:
            print("Invalid input please try again.")



def has_max_jobs():
    count = 0
    for line in open("jobs.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted jobs have been posted, please come back later." + "\n")
        return True
    return False




def createNewJob():
    print("")
    title = input("Enter the title for your job: ")
    description = input("Enter the description for your job: ")
    employer = input("Enter the employer for your job: ")
    location = input("Enter the location for your job: ")
    salary = input("Enter the salary for your job: ")

    saveJob(title, description, employer, location, salary)


def saveJob(t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()


#postNewJob()