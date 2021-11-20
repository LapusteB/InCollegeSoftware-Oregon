import epic10


def test_applied_jobs_output():
    job = open("appliedJobs.txt", "r")
    lines = job.readlines()
    job.close()

    account = open("accounts.txt", "w")
    account.write("Student Learner\n")
    account.close()

    jobs = open("appliedJobs.txt", "w")
    jobs.write("Student Learner	library worker	A	B	C	D\n")
    jobs.close()

    epic10.apply_appliedJobsAPI('library worker', 'Student Learner', 'C')

    jobLine = open("appliedJobs.txt", "w")
    for line in lines:
        jobLine.write(line)
    jobLine.close()

    output = open("MyCollege_jobs.txt", "r").readlines()
    assert output == ["Student Learner	library worker	A	B	C	D\n",
                      "=====\n"]


def test_Student_Accounts_API():
    file = open("studentAccounts.txt", "w")
    file.write("username\tfname lname\npassword")
    file.close()

    open("accounts.txt", "w").close()
    open("usernames.txt", "w").close()
    open("passwords.txt", "w").close()

    epic10.studentAccountAPI()

    name = open("accounts.txt", "r").readlines()
    username = open("usernames.txt", "r").readlines()
    password = open("passwords.txt", "r").readlines()

    output = name + username + password
    assert output == ['fname lname\n', 'username\n', 'password\n']


def test_Jobs_API():
    jobs = open("newJobs.txt", "w")
    jobs.write("title\ndescription&&&\nposter\nemployer\nlocation\nsalary\n")
    jobs.close()

    open("jobs.txt", "w").close()
    epic10.newJobsAPI()
    output = open("jobs.txt", "r").readlines()
    assert output == ['poster\ttitle\tdescription&&&\temployer\tlocation\tsalary\n']


def test_Training_API():
    training = open("newtraining.txt", "w")
    training.write("training1\ntraining2\ntraining3\ntraining4\n")
    training.close()
    open("training.txt", "w").close()
    epic10.trainingAPI()


    output = open("training.txt", "r").readlines()
    assert output == ['training1\n', 'training2\n', 'training3\n', 'training4\n']

