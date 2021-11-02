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