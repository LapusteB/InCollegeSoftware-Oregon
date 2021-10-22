import builtins
import login

input_values = []
print_values = []

def test_save_jobs():
    jobs = open("jobs.txt", "r").readlines()
    savedJobs = open("savedJobs.txt", "r").readlines()
    jobs0 = open("savedJobs.txt", "w")
    jobs0.write("\nStudent Learner\tworker\twork alot\tusf\ttampa\t1")
    jobs0.close()
    savedJobs0 = open("savedJobs.txt", "w")
    savedJobs0.close()

    set_keyboard_input(["user", "P@ssword1", "3", "s", "1", "1", "-1", "-1", "0", "0", "0"])
    login.login("Student Learner")

    insertSuccess = False
    testedSavedJob = open("savedJobs.txt", "r")
    for line in testedSavedJob:
        if line != '\n':
            s, j = line.split('\t')
            if s == "Student Learner":
                if j == "worker\n":
                    insertSuccess = True
                    break
    testedSavedJob.close()

    jobs1 = open("jobs.txt", "w")
    for job in jobs:
        jobs1.write(job)
    jobs1.close()

    savedJobs1 = open("savedJobs.txt", "w")
    for savedJob in savedJobs:
        savedJobs1.write(savedJob)
    savedJobs1.close()

    assert insertSuccess


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