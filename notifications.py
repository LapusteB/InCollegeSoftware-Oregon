from datetime import date, datetime


def createProfileNotification(username):
    profileFile = open("profile.txt", "r")
    for profile in profileFile:
        if profile != '\n':
            name, a, b, c, d = profile.split('\t')
            if name == username:
                return True

    print("NOTIFICATION: Don't forget to create a profile!")
    return False


def numberOfAppliedJobsNotification(username):
    numberOfJobs = 0
    appliedJobs = open("appliedJobs.txt", "r")
    for job in appliedJobs:
        if job != '\n':
            name, a, b, c, d = job.split('\t')
            if name == username:
                numberOfJobs += 1
    print("")
    print(f"NOTIFICATION: You have currently applied for {numberOfJobs} jobs")
    print("")

#checks date applied for job and compares to current date
def checkLastJobAppliedNotification(username):
    today = date.today()
    temp = today.strftime("%m/%d/%Y")
    todaysDate = datetime.strptime(temp, "%m/%d/%Y")

    appliedJobs = open("appliedJobs.txt", "r")
    for line in appliedJobs:
        if line != '\n':
            name, a, b, c, d, dateApplied = line.split('\t')
            lastApplied = datetime.strptime(dateApplied, "%d/%m/%Y")
            if name == username and (lastApplied - todaysDate).days < 7:
                return True

    return False

