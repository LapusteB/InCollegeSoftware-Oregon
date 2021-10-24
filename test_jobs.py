import builtins
import login
import views
import testBaseEpic6

input_values = []
print_values = []

def test_save_jobs():
    jobs = open("jobs.txt", "r").readlines()
    savedJobs = open("savedJobs.txt", "r").readlines()

    jobs0 = open("savedJobs.txt", "w")
    jobs0.write("Student Learner2\tworker\tD\tE\tL\tS")
    jobs0.close()

    savedJobs0 = open("savedJobs.txt", "w")
    savedJobs0.close()

    set_keyboard_input(["3", "s", "1", "-1", "-1", "0", "0", "0"])
    views.mainPage("Student Learner")

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


def test_applied_jobs_indicator():
    jobs = open("jobs.txt", "r").readlines()
    appliedJobs = open("appliedJobs.txt", "r").readlines()
    savedJobs = open("savedJobs.txt", "r").readlines()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("\nStudent Learner2\tengineering worker\tD\tE\tL\tS")
    jobs0.close()
    appliedJobs0 = open("appliedJobs.txt", "w")
    appliedJobs0.write("Student Learner\tengineering worker\tstart date\tendate\tdes")
    appliedJobs0.close()
    savedJobs0 = open("savedJobs.txt", "w")
    savedJobs0.close()

    set_keyboard_input(["3", "-1", "0", "0", "0"])
    views.mainPage("Student Learner")

    output = get_display_output()

    jobs1 = open("jobs.txt", "w")
    for job in jobs:
        jobs1.write(job)
    jobs1.close()

    appliedJobs1 = open("appliedJobs.txt", "w")
    for appliedJob in appliedJobs:
        appliedJobs1.write(appliedJob)
    appliedJobs1.close()

    savedJobs1 = open("savedJobs.txt", "w")
    for savedJob in savedJobs:
        savedJobs1.write(savedJob)
    savedJobs1.close()

    assert output == ["",
                      "*************",
                      "* InCollege *",
                      "*************",
                      "",
                      "Main page",
                      "------------------------------------",
                      "| '1' to find someone you know      |",
                      "| '2' for learn new skill           |",
                      "| '3' for job search/ internship    |",
                      "| '4' for useful links              |",
                      "| '5' to go to your profile         |",
                      "| '6' to show your network          |",
                      "| '7' to show your friendList       |",
                      "| '0' to return to login            |",
                      "-------------------------------------",
                      "",
                      "Enter page you want to go to: ",
                      "\n",
                      "Job Search/ Internship",
                      "------------------------------------",
                      "List of all jobs",
                      "1. engineering worker (applied)",
                      "Enter 'a' to appy for jobs, Enter 's' to save jobs, 'u' to unmark a job or enter -1 to to see more options: ",
                      "------------------------------------",
                      "Press '0' to return to mainPage, '1' to post a new job, '2' to generate list of jobs applied, '3' to generate list of saved jobs or  '4' to generate list of jobs that you have not applied yet: ",
                      "",
                      "*************",
                      "* InCollege *",
                      "*************",
                      "",
                      "Main page",
                      "------------------------------------",
                      "| '1' to find someone you know      |",
                      "| '2' for learn new skill           |",
                      "| '3' for job search/ internship    |",
                      "| '4' for useful links              |",
                      "| '5' to go to your profile         |",
                      "| '6' to show your network          |",
                      "| '7' to show your friendList       |",
                      "| '0' to return to login            |",
                      "-------------------------------------",
                      "",
                      "Enter page you want to go to: ",
                      "",
                      "*************",
                      "* InCollege *",
                      "*************",
                      "",
                      "Main page",
                      "------------------------------------",
                      "| '1' to find someone you know      |",
                      "| '2' for learn new skill           |",
                      "| '3' for job search/ internship    |",
                      "| '4' for useful links              |",
                      "| '5' to go to your profile         |",
                      "| '6' to show your network          |",
                      "| '7' to show your friendList       |",
                      "| '0' to return to login            |",
                      "-------------------------------------",
                      "",
                      "Enter page you want to go to: "]


def test_show_jobs():
    jobs = open("jobs.txt", "r").readlines()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("\nStudent Learner\tworker\twork alot\tusf\ttampa\t1")
    jobs0.close()

    savedJobs = open("savedJobs.txt", "r").readlines()
    savedJobs0 = open("savedJobs.txt", "w")
    savedJobs0.close()

    appliedJobs = open("appliedJobs.txt", "r").readlines()
    appliedJobs0 = open("appliedJobs.txt", "w")
    appliedJobs0.close()

    set_keyboard_input(["3", "-1", "0", "0", "0", "0"])
    views.mainPage("Student Learner")

    output = get_display_output()

    jobs1 = open("jobs.txt", "w")
    for job in jobs:
        jobs1.write(job)
    jobs1.close()

    savedJobs1 = open("savedJobs.txt", "w")
    for savedJob in savedJobs:
        savedJobs1.write(savedJob)
    savedJobs1.close()

    appliedJobs1 = open("appliedJobs.txt", "w")
    for appliedJob in appliedJobs:
        appliedJobs1.write(appliedJob)
    appliedJobs1.close()

    assert output == ["",
                      "*************",
                      "* InCollege *",
                      "*************",
                      "",
                      "Main page",
                      "------------------------------------",
                      "| '1' to find someone you know      |",
                      "| '2' for learn new skill           |",
                      "| '3' for job search/ internship    |",
                      "| '4' for useful links              |",
                      "| '5' to go to your profile         |",
                      "| '6' to show your network          |",
                      "| '7' to show your friendList       |",
                      "| '0' to return to login            |",
                      "-------------------------------------",
                      "",
                      "Enter page you want to go to: ",
                      "\n",
                      "Job Search/ Internship",
                      "------------------------------------",
                      "List of all jobs",
                      "1. worker",
                      "Enter 'a' to appy for jobs, Enter 's' to save jobs, 'u' to unmark a job or enter -1 to to see more options: ",
                      "------------------------------------",
                      "Press '0' to return to mainPage, '1' to post a new job, '2' to generate list of jobs applied, '3' to generate list of saved jobs or  '4' to generate list of jobs that you have not applied yet: ",
                      "",
                      "*************",
                      "* InCollege *",
                      "*************",
                      "",
                      "Main page",
                      "------------------------------------",
                      "| '1' to find someone you know      |",
                      "| '2' for learn new skill           |",
                      "| '3' for job search/ internship    |",
                      "| '4' for useful links              |",
                      "| '5' to go to your profile         |",
                      "| '6' to show your network          |",
                      "| '7' to show your friendList       |",
                      "| '0' to return to login            |",
                      "-------------------------------------",
                      "",
                      "Enter page you want to go to: ",
                      "",
                      "*************",
                      "* InCollege *",
                      "*************",
                      "",
                      "Main page",
                      "------------------------------------",
                      "| '1' to find someone you know      |",
                      "| '2' for learn new skill           |",
                      "| '3' for job search/ internship    |",
                      "| '4' for useful links              |",
                      "| '5' to go to your profile         |",
                      "| '6' to show your network          |",
                      "| '7' to show your friendList       |",
                      "| '0' to return to login            |",
                      "-------------------------------------",
                      "",
                      "Enter page you want to go to: "]


def test_apply_to_job():
    jobs = open("jobs.txt", "r").readlines()
    appliedJobs = open("appliedJobs.txt", "r").readlines()
    savedJobs = open("savedJobs.txt", "r").readlines()

    jobs0 = open("jobs.txt", "w")
    jobs0.write("\nStudent Learner2\tengineering worker\tD\tE\tL\tS")
    jobs0.close()
    appliedJobs0 = open("appliedJobs.txt", "w")
    appliedJobs0.close()
    savedJobs0 = open("savedJobs.txt", "w")
    savedJobs0.close()

    set_keyboard_input(["3", "a", "engineering worker", "05/31/2022", "06/01/2022", "Smart boi", "-1", "0", "0", "0"])
    views.mainPage("Student Learner")

    insertSuccess = True
    applied = open("appliedJobs.txt", "r")
    for line in applied:
        if line != '\n':
            s, j, d, e, f = line.split('\t')
            if s == "Student Learner":
                if j == "engineering worker\n":
                    if d == "05/31/2022":
                        if e == "06/01/2022":
                            if f == "Smart boi":
                                insertSuccess = True
                                break

    jobs1 = open("jobs.txt", "w")
    for job in jobs:
        jobs1.write(job)
    jobs1.close()

    appliedJobs1 = open("appliedJobs.txt", "w")
    for appliedJob in appliedJobs:
        appliedJobs1.write(appliedJob)
    appliedJobs1.close()

    savedJobs1 = open("savedJobs.txt", "w")
    for savedJob in savedJobs:
        savedJobs1.write(savedJob)
    savedJobs1.close()


def test_job_description():
    jobs = open("jobs.txt", "r").readlines()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("Student Learner2\tworker\tD\tE\tL\tS")
    jobs0.close()

    set_keyboard_input(["1"])
    testBaseEpic6.displayJob("worker")
    output = get_display_output()

    jobs1 = open("jobs.txt", "w")
    for job in jobs:
        jobs1.write(job)
    jobs1.close()

    assert output == ["",
                      "\n----------JOB DESCRIPTION----------",
                      "Title: worker",
                      "Description: D",
                      "Employer: E",
                      "Location: L",
                      "Salary: S"]


def test_applied_jobs_got_deleted():
    print_values.clear()
    fr = open("appliedJobsDeleted.txt", "w")
    fr.write("Student Learner\tSoftware Engineer\n")
    fr.close()
    
    testBaseEpic6.check_if_applied_jobs_got_deleted("Student Learner")

    output = get_display_output()

    assert output == ["Here are the job(s) You've applied for has(have) been deleted:",
                        "Software Engineer",
                        "------------------------------------"]


def test_has_max_jobs():
    un = open("jobs.txt", "r").readlines()
    file = open("jobs.txt", "w")

    isTrue = False

    for i in range(1,11):
        file.write("${i}\n")
    file.close()
    isTrue = views.has_max_jobs()

    file1 = open("jobs.txt", "w")
    for line in un:
        file1.write(line)
    file1.close()

    assert isTrue

def test_appliedjoblist():
    print_values.clear()
    appliedJobs = open("appliedJobs.txt", "w")
    appliedJobs.write("Student Learner\tworker\tstart date\tendate\tdes")
    appliedJobs.close()

    testBaseEpic6.appliedJobListGenerate("Student Learner")

    output = get_display_output()

    assert output == ["List of applied jobs:", "worker", "------------------------------------"]

def test_notappliedjoblist():
    print_values.clear()
    appliedJobs = open("appliedJobs.txt", "w")
    appliedJobs.write("Student Learner\tworker\tstart date\tendate\tdes")
    appliedJobs.close()

    jobs = open("jobs.txt","w")
    jobs.write("Student Learner2\tengineering worker\tD\tE\tL\tS")
    jobs.close()

    testBaseEpic6.notAppliedJobsListGenerator("Student Learner")

    output = get_display_output()

    assert output == ["List of jobs that has been applied to:", "engineering worker", "------------------------------------"]

def test_savedjoblist():
    print_values.clear()
    appliedJobs = open("savedJobs.txt", "w")
    appliedJobs.write("Student Learner\tsaved worker")
    appliedJobs.close()

    testBaseEpic6.savedJobListGenerate("Student Learner")

    output = get_display_output()

    assert output == ["List of saved jobs:", "saved worker", "------------------------------------"]

def test_applypostedjobs():
    postedJobs = open("jobs.txt", "w")
    postedJobs.write("Student Learner\tworker\tD\tE\tL\tS")
    postedJobs.close()

    set_keyboard_input(["worker"])
    testBaseEpic6.checkApplyJobs("Student Learner")

    output = get_display_output()

    assert output == ["Enter the name of the job you want to apply to: ",
                        "Error, You listed this job as an employer: Student Learner" ]

def test_applyappliedjobs():
    appliedJobs = open("appliedJobs.txt", "w")
    appliedJobs.write("Student Learner\tworker\tstart date\tendate\tdes")
    appliedJobs.close()

    set_keyboard_input(["worker"])
    testBaseEpic6.checkApplyJobs("Student Learner")

    output = get_display_output()

    assert output == ["Enter the name of the job you want to apply to: ",
                        "Error, You have already applied to this job: worker" ]

def test_deletejobs():
    Jobs = open("jobs.txt", "w")
    Jobs.write("Student Learner\tworker\tD\tE\tL\tS")
    Jobs.close()

    set_keyboard_input(["worker"])
    views.deleteJOB()

    jobs = open("jobs.txt", "r").readlines()

    assert len(jobs) == 0


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