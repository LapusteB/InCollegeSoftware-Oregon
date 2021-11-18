from itertools import groupby


def output_jobs():
    aFile = open("jobs.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    wFile = open("MyCollege_jobs.txt", "w")
    for line in lines:
        if line != '\n':
            wFile.write(line)
            wFile.write("=====" + '\n')
    wFile.close()
    return


def output_userProfiles():
    aFile = open("profile.txt", "r")
    linea = aFile.readlines()
    aFile.close()

    bFile = open("profile_education.txt", "r")
    lineb = bFile.readlines()
    bFile.close()

    cFile = open("profile_experience.txt", "r")
    linec = cFile.readlines()
    cFile.close()

    wFile = open("profiletempFile.txt", "w")
    for line in linea:
        if line != '\n':
            wFile.write(line)
    wFile.close()

    wbFile = open("profiletempFile.txt", 'a')
    for line in lineb:
        if line != '\n':
            wbFile.write(line)

    wbFile.close()

    wcFile = open("profiletempFile.txt", 'a')
    for line in linec:
        if line != '\n':
            wcFile.write(line)
    wcFile.close()

    wFile = open("MyCollege_profiles.txt", "w")
    with open("profiletempFile.txt") as f:
        lines = ((line.split(None, 1)[:1], line) for line in f if line.strip())

        for k, g in groupby(lines, lambda L: L[0]):
            lines = [el[1] for el in g]
            lines.sort()
            for li in lines:
                wFile.write(li)
            wFile.write("=====" + '\n')
    wFile.close()


def output_users():
    aFile = open("accounts.txt", "r")
    lines = aFile.readlines()
    aFile.close()

    wFile = open("MyCollege_users.txt", "w")
    for line in lines:
        if line != '\n':
            wFile.write(line)
    wFile.close()


def output_training():
    wFile = open("MyCollege_training.txt", "w")
    with open("learning.txt") as f:
        lines = ((line.split(None, 1)[:1], line) for line in f if line.strip())

        for k, g in groupby(lines, lambda L: L[0]):
            lines = [el[1] for el in g]
            lines.sort()
            for li in lines:
                wFile.write(li)
            wFile.write("=====" + '\n')
    wFile.close()


def output_savedJobs():
    wFile = open("MyCollege_savedJobs.txt", "w")
    with open("savedJobs.txt") as f:
        lines = ((line.split(None, 1)[:1], line) for line in f if line.strip())

        for k, g in groupby(lines, lambda L: L[0]):
            lines = [el[1] for el in g]
            lines.sort()
            for li in lines:
                wFile.write(li)
            wFile.write("=====" + '\n')
    wFile.close()
