import outputApi
import epic10
from validatePass import validatePass
import notifications

def createNewJob():
    print("")
    title = input("Enter the title for your job: ")
    description = input("Enter the description for your job: ")
    employer = input("Enter the employer for your job: ")
    location = input("Enter the location for your job: ")
    salary = input("Enter the salary for your job: ")
    name = "Student Learner"

    saveJob(name, title, description, employer, location, salary)
    epic10.post_appliedJobsAPI(title)
    outputApi.output_jobs()
    newJobPosted(name, title)
    print("\nyour job has been saved")
    return


def saveJob(n, t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(n + "\t" + t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()


def newJobPosted(username, title):
    file1 = open("accounts.txt", "r")
    file2 = open("newJobPosted.txt", "w")

    for line in file1:
        if username not in line:
            line = line.strip('\n')
            file2.write(line + "\t" + title + "\n")
    file1.close()
    file2.close()


def deleteJOB():
    print("\n----------JOB DELETION--------")
    sel = input("Enter the name of the job you want to delete: ")
    a_file = open("jobs.txt", "r")

    lines = a_file.readlines()
    a_file.close()

    for i in lines:  # sel in lines
        if sel in i:
            lines.remove(i)

            # put deleted jobs in appliedJobs
            # open the applied jobs, get all the jobs
            f = open("appliedJobs.txt", 'r')
            for l in f:
                if l != '\n':
                    l = l.rstrip()
                    n, t, start, end, des, e = l.split('\t')
                    # if the title is the same put in the appliedJobsDeleted
                    if t == sel:
                        epic10.delete_appliedJobsAPI(t)
                        print("deleted")
                        job_got_deleted_notification(n, t)

            # close file
            f.close()

    new_file = open("jobs.txt", "w+")
    for line in lines:
        new_file.write(line)

    new_file.close()

    outputApi.output_jobs()

    print("-----JOB Deleted------\n")


def job_got_deleted_notification(userName,jobName):
    appliedJobsGotDeletedFile = open("appliedJobsDeleted.txt",'a')
    appliedJobsGotDeletedFile.write(userName + '\t' + jobName +'\n')
    appliedJobsGotDeletedFile.close()


def register():
    print("-----------------------------")
    print("Welcome to the InCollege App!")
    print("-----------------------------")
    file = open("usernames.txt", "a")  # - file will be created if not present
    file2 = open("passwords.txt", "a")  # - file will be created if not present
    file3 = open("accounts.txt", "a")
    # Checks if there are already 5 accounts made this way
    if has_max_users():
        return

    # Checks if there is a duplicate username
    print("(Press '0' to return)")
    u = input("Please enter a unique username: ")
    if username_exists(u):
        print("Error, Username already created! Returning home")
        return

    if u == "0":
        return

    file.write(u + "\n")
    print(
        "Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
    p = input("Please enter a valid password: ")
    res = validatePass(p)

    while res is False:
        if res is False:
            print("Error, Please meet password requirements:")
            print("---------------------------------------------")
            print("-minimum of 8 characters")
            print("-maximum of 12 characters")
            print("-at least one capital letter")
            print("-one digit, one non-alpha character")
            print("---------------------------------------------")
        p = input("Re-enter Password: ")
        res = validatePass(p)
    file2.write(p + "\n")
    Fname = input("What is your first name?: ")
    Lname = input("What is your last name?: ")

    print("-------------------------------------------------")
    plus = input("- Do you want to register as a PLUS member? (y/n): ")
    if plus == "y":
        Fname = Fname + "++"
    print("-------------------------------------------------")

    file3.write(Fname + " " + Lname + "\n")

    file.close()
    file2.close()
    file3.close()

    outputApi.output_users()
    nameofuser = Fname + " " + Lname

    print("\nHello, " + Fname)
    print("Account Created!")
    print("Entering main page....")
    notifications.addNotificationsForNewUser(Fname, Lname)
    return


def has_max_users():
    count = 0
    for line in open("usernames.txt", "r"): count += 1
    if count == 10 or count > 10:
        print("All permitted accounts have been created, please come backlater")
        return True
    return False


def username_exists(u):
    with open('usernames.txt') as f:
        if u in f.read():
            return True
        return False


def Train(name):
    if(taken_Train(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        if(decision == 'y'):
            print("You have now completed this training\n")
        elif(decision == 'n'):
            print("Course Cancelled\n")
        else:
            print("Please enter valid input\n")
    else:
        learningfile = open("learning.txt", 'a')
        learningfile.write(name + '\t' + "Train the trainer" + '\n')
        learningfile.close()
        outputApi.output_training()
        print("You have now completed this training")


def taken_Train(name):
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')

            if (u == name and i == "Train the trainer" + '\n'):
                return True
    return False