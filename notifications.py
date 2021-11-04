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
            name, a, b, c, d, dateApplied = job.split('\t')
            name, a, b, c, d, e = job.split('\t')
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
            dateApplied = dateApplied.strip('\n')
            lastApplied = datetime.strptime(dateApplied, "%m/%d/%Y")
            if name == username and (todaysDate - lastApplied).days > 6:
                return True

    return False

#notifies if new job has been posted
def newJobPostedNotification(username):
    file = open("newJobPosted.txt", "r")
    t = username
    for line in file:
        if line != '\n':
            if t in line:
                return True

    return False


#removes job posted notification when user checks jobs
def removeJobPostedNotification(username):
    file = open("newJobPosted.txt", "r")
    removal = file.readlines()
    file.close()
    copy = open("newJobPosted.txt", "w")

    for line in removal:
        if username not in line:
            copy.write(line)


def getTitleForJobNotification(username):
    file = open("newJobPosted.txt", "r")
    for line in file:
        if line != '\n':
            name, title = line.split('\t')
            if name == username:
                title = title.strip('\n')
                return title

def addNotificationsForNewUser(first, last):
    file = open("accounts.txt", "r")
    file1 = open("newStudentNotification.txt", "w")
    fullName = first + " " + last
    for line in file:
        if line != '\n' and fullName not in line:
            line = line.strip('\n')
            file1.write(line + '\t' + first + '\t' + last + '\n')


def checkNotificationsForNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            if name == username:
                return True
    return False

def returnFirstNameOfNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            notifFirstName = notifFirstName.strip('\n')
            if name == username:
                return notifFirstName

def returnLastNameOfNewUser(username):
    file = open("newStudentNotification.txt", "r")

    for line in file:
        if line != '\n':
            name, notifFirstName, notifLastName = line.split('\t')
            notifLastName = notifLastName.strip('\n')
            if name == username:
                return notifLastName

def removeNewUserNotification(username):
    file = open("newStudentNotification.txt", "r")
    fileRead = file.readlines()
    file.close

    file1 = open("newStudentNotification.txt", "w")

    for line in fileRead:
        if username not in line:
            file1.write(line)
