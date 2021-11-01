def createProfileNotification(username):
    profileFile = open("profile.txt", "r")
    for profile in profileFile:
        if profile != '\n':
            name, a, b, c, d = profile.split('\t')
            if name == username:
                return True

    print("NOTIFICATION: Don't forget to create a profile!")
    return False
