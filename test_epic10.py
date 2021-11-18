import outputApi


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
