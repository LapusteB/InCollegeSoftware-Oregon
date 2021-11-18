import outputApi
import epic10_test_base
import builtins
import views

input_values = []
print_values = []

def test_my_college_jobs():
    jobs = open("jobs.txt", "r")
    jobList = jobs.readlines()
    jobs.close()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("Student Learner2\tengineering worker\tD\tE\tL\tS\nStudent Learner\tlibrary worker\tA\tB\tC\tD\n")
    jobs0.close()

    outputApi.output_jobs()

    job = open("jobs.txt", "w")
    for line in jobList:
        if line != "\n":
            job.write(line)
    job.close()

    myCollegeJobs = open("MyCollege_jobs.txt", "r").readlines()
    assert myCollegeJobs == ["Student Learner2\tengineering worker\tD\tE\tL\tS\n",
                             "=====\n",
                             "Student Learner\tlibrary worker\tA\tB\tC\tD\n",
                             "=====\n"]


def test_job_create_output():
    jobs = open("jobs.txt", "r")
    jobList = jobs.readlines()
    jobs.close()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("Student Learner2\tengineering worker\tD\tE\tL\tS\nStudent Learner\tlibrary worker\tA\tB\tC\tD\n")
    jobs0.close()

    set_keyboard_input(["Tester", "Test Functions", "USF", "Tampa", "1"])
    epic10_test_base.createNewJob()

    job = open("jobs.txt", "w")
    for line in jobList:
        if line != "\n":
            job.write(line)
    job.close()

    myCollegeJobs = open("MyCollege_jobs.txt", "r").readlines()
    assert myCollegeJobs == ["Student Learner2\tengineering worker\tD\tE\tL\tS\n",
                             "=====\n",
                             "Student Learner\tlibrary worker\tA\tB\tC\tD\n",
                             "=====\n",
                             "Student Learner\tTester\tTest Functions\tUSF\tTampa\t1\n",
                             "=====\n"]


def test_jobs_deleted_output():
    jobs = open("jobs.txt", "r")
    jobList = jobs.readlines()
    jobs.close()
    appliedJobs = open("appliedJobs.txt", "r")
    applyList = appliedJobs.readlines()
    appliedJobs.close()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("Student Learner2\tengineering worker\tD\tE\tL\tS\nStudent Learner\tlibrary worker\tA\tB\tC\tD\n")
    jobs0.close()
    apply = open("appliedJobs.txt", "w")
    apply.close()

    set_keyboard_input(["engineering worker"])
    epic10_test_base.deleteJOB()

    job = open("jobs.txt", "w")
    for line in jobList:
        if line != "\n":
            job.write(line)
    job.close()

    app = open("appliedJobs.txt", "w")
    for ap in applyList:
        if ap != "\n":
            app.write(ap)
    app.close()

    myCollegeJobs = open("MyCollege_jobs.txt", "r").readlines()
    assert myCollegeJobs == ["Student Learner\tlibrary worker\tA\tB\tC\tD\n",
                             "=====\n"]


def test_profile_output():
    aFile = open("profile.txt", "r")
    linea = aFile.readlines()
    aFile.close()

    bFile = open("profile_education.txt", "r")
    lineb = bFile.readlines()
    bFile.close()

    cFile = open("profile_experience.txt", "r")
    linec = cFile.readlines()
    cFile.close()

    profile = open("profile.txt", "w")
    profile.write("Student2 Learner2\ttitle	Major\tUniversity\tabout me\n")
    profile.close()

    education = open("profile_education.txt", "w")
    education.write("Student2 Learner2\tusf\tcs\t2018\n")
    education.close()

    experience = open("profile_experience.txt", "w")
    experience.write("Student2 Learner2\ttitle\te\tds\tde\tl\td\n")
    experience.close()

    outputApi.output_userProfiles()

    profiles = open("profile.txt", "w")
    for line in linea:
        if line != "\n":
            profiles.write(line)
    profiles.close()

    educations = open("profile_education.txt", "w")
    for line in lineb:
        if line != "\n":
            educations.write(line)
    educations.close()

    experiences = open("profile_experience.txt", "w")
    for line in linec:
        if line != "\n":
            experiences.write(line)
    experiences.close()

    myCollegeProfiles = open("MyCollege_profiles.txt", "r").readlines()
    assert myCollegeProfiles == ["Student2 Learner2\ttitle\tMajor\tUniversity\tabout me\n",
                                 "Student2 Learner2\ttitle\te\tds\tde\tl\td\n",
                                 "Student2 Learner2\tusf\tcs\t2018\n",
                                 "=====\n"]


def test_users_output():
    aFile = open("accounts.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    accounts = open("accounts.txt", "w")
    accounts.write("tester one\ntester two\n")
    accounts.close()

    outputApi.output_users()

    account = open("accounts.txt", "w")
    for line in lines:
        account.write(line)
    account.close()

    users = open("MyCollege_users.txt", "r").readlines()
    assert users == ["tester one\n",
                     "tester two\n"]


def test_users_added_ouput():
    aFile = open("accounts.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    bFile = open("usernames.txt", "r")
    linesa = bFile.readlines()
    bFile.close()

    cFile = open("passwords.txt", "r")
    linesc = cFile.readlines()
    cFile.close()

    accounts = open("accounts.txt", "w")
    accounts.write("tester one\ntester two\n")
    accounts.close()

    set_keyboard_input(["LastTester", "Abcdef1!!!!", "Final", "Tester", "n"])
    epic10_test_base.register()

    account = open("accounts.txt", "w")
    for line in lines:
        account.write(line)
    account.close()

    user = open("usernames.txt", "w")
    for use in linesa:
        user.write(use)
    user.close()

    password = open("passwords.txt", "w")
    for passW in linesc:
        password.write(passW)
    password.close()

    users = open("MyCollege_users.txt", "r").readlines()
    assert users == ["tester one\n",
                     "tester two\n",
                     "Final Tester\n"]


def test_training_output():
    learn = open("learning.txt", "r")
    lines = learn.readlines()
    learn.close()

    learning = open("learning.txt", "w")
    learning.write("test1\tUnderstanding the Architectural desing Process\ntest2\tHow to pass the class\n")
    learning.close()

    outputApi.output_training()

    learningF = open("learning.txt", "w")
    for line in lines:
        learningF.write(line)
    learningF.close()

    outputFile = open("MyCollege_training.txt", "r").readlines()
    assert outputFile == ["test1\tUnderstanding the Architectural desing Process\n",
                          "=====\n",
                          "test2\tHow to pass the class\n",
                          "=====\n"]


def test_training_add_ouptut():
    learn = open("learning.txt", "r")
    lines = learn.readlines()
    learn.close()

    learning = open("learning.txt", "w")
    learning.write("test1\tUnderstanding the Architectural design Process\ntest2\tHow to pass the class\n")
    learning.close()

    epic10_test_base.Train("tester")

    learningF = open("learning.txt", "w")
    for line in lines:
        learningF.write(line)
    learningF.close()

    outputFile = open("MyCollege_training.txt", "r").readlines()
    assert outputFile == ["test1\tUnderstanding the Architectural design Process\n",
                          "=====\n",
                          "test2\tHow to pass the class\n",
                          "=====\n",
                          "tester\tTrain the trainer\n",
                          "=====\n"]


def test_saved_jobs_output():
    job = open("savedJobs.txt", "r")
    lines = job.readlines()
    job.close()

    jobs = open("savedJobs.txt", "w")
    jobs.write("Student Learner\tsaved worker\nAnother Tester\tsaved job\n")
    jobs.close()

    outputApi.output_savedJobs()

    jobLine = open("savedJobs.txt", "w")
    for line in lines:
        jobLine.write(line)
    jobLine.close()

    output = open("MyCollege_savedJobs.txt", "r").readlines()
    assert output == ["Student Learner\tsaved worker\n",
                      "=====\n",
                      "Another Tester\tsaved job\n",
                      "=====\n"]


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