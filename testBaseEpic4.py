#This is for testing.....
from os import name
import usefulLinks
import profile
from re import DOTALL
import csv


def mainPage(nameofuser):
    global name
    name = nameofuser

    kbInput = '-1'

    while (kbInput != '0'):
        print("")
        print("*************")
        print("* InCollege *")
        print("*************")
        print("")
        print("Main page")
        print("------------------------------------")
        print("| '1' to find someone you know      |")
        print("| '2' for learn new skill           |")
        print("| '3' for job search/ internship    |")
        print("| '4' for useful links              |")
        print("| '5' to go to your profile         |")
        print("| '0' to return to login            |")
        print("-------------------------------------")
        print("")
        kbInput = input("Enter page you want to go to: ")

        if (kbInput == '1'):
            peopleSearchPage()
        elif (kbInput == '2'):
            skillsPage()
        elif (kbInput == '3'):
            jobSearchPage()
        elif (kbInput == '4'):
            usefulLinks.menu()
        elif (kbInput == '5'):
            profile.profileMenu(name)
        elif (kbInput == '0'):
            return
        else:
            print("Please enter an available option!!\n")
def postNewJob():
    select = "x"
    print("-----------------------------------")
    print(" Welcome to the Job Creation Page! ")
    print("-----------------------------------")
    while (select != 'y' and select != 'Y' and select != 'n' and select != "N"):
        select = input("Would you like to create a job? ('y' or 'n'): ")
        if (select == 'y' or select == 'Y'):
            if (has_max_jobs()):
                mainPage()
            createNewJob()
        elif (select == 'n' or select == 'N'):
            mainPage()
        else:
            print("Invalid input please try again.")


def has_max_jobs():
    count = 0
    for line in open("jobs.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted jobs have been posted, please come back later." + "\n")
        return True
    return False


def createNewJob():
    print("")
    title = input("Enter the title for your job: ")
    description = input("Enter the description for your job: ")
    employer = input("Enter the employer for your job: ")
    location = input("Enter the location for your job: ")
    salary = input("Enter the salary for your job: ")

    saveJob(name, title, description, employer, location, salary)

    print("\nyour job has been saved")
    mainPage(name)


def saveJob(n, t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(n + "\t" + t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()


def peopleSearchPage():
    a = -1
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    file3 = open("accounts.txt", "r")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname

    from login import find_contacts

    if (find_contacts(name)):
        print("")
        print("They are a part of the InCollege system." + "\n")
        mainPage()
    else:
        print("")
        print("They are not a part of the InCollege system" + "\n")
        mainPage()
    a = input("Press '0' to return.")
    if int(a) == 0:
        mainPage()

    file3.close()


def skillsPage():
    kbInput = "6"

    while (kbInput != "1" and kbInput != "2"
           and kbInput != "3" and kbInput != "4" and kbInput != "5" and kbInput != "b"):
        print("--------------------------------------------------------")
        print("Available skills to learn:")
        print("Enter the Coressponding Number with a skill to learn it today:")
        print(" 1. LeaderShip")
        print(" 2. Basic programming in Python")
        print(" 3. Make an outstanding resume")
        print(" 4. Professional writing")
        print(" 5. Microsoft Excel basics")
        kbInput = input(" Or enter b for return to mainPage\n")

        if (kbInput != "1" and kbInput != "2"
                and kbInput != "3" and kbInput != "4" and kbInput != "5" and kbInput != "b"):
            print("Please enter the available options")
        elif (kbInput != "b"):
            print("Page under construction.")
            a = input("Press '0' to return")
            if int(a) == 0:
                mainPage(name)

    if (kbInput == "b"):
        mainPage(name)


def jobSearchPage():
    print("\n")
    print("Job Search")
    print("------------")
    a = "x"

    while (a != "0" and a != "1"):
        a = input("Press '0' to return or 1 to post a new job.")
        if a == "0":
            mainPage(name)
        elif (a == "1"):
            postNewJob()
        else:
            print("Please enter an available option!!\n")


def pageUnderConstruction():
    print("")
    print("--------------------------------------------------------")
    print("Page under construction")































class Profile:
    def __init__(self, name, title, major, university, about):
        self.name = name
        self.title = title
        self.major = major
        self.university = university
        self.about = about

class Experience:
    def __init__(self, username, title, employer, date_started, date_ended, location, description):
        self.username = username
        self.title = title
        self.employer = employer
        self.date_started = date_started
        self.date_ended = date_ended
        self.location = location
        self.description = description

    def __eq__(self, other):
        return self.username == other.username and self.title == other.title and self.employer == other.employer

class Education:
    def __init__(self, username, school, degree, years):
        self.username = username
        self.school = school
        self.degree = degree
        self.years = years
    def __eq__(self, other):
        return self.username == other.username and self.school == other.school and self.degree == other.degree   

def profileMenu(username):
    global profileList, profileExists, user, experienceList, educationList
    user = username
    profileExists = False
    profileList = []
    experienceList = []
    educationList = []
    userProfile = Profile(username, "", "", "", "")
    

    profileFile = open("profile.txt", "r")
    for line in profileFile:
        if line != '\n':
            u, t, n, m, p = line.split('\t')
            profile = Profile(u, t, n, m, p)
            profileList.append(profile)
            if (profile.name == username):
                userProfile = profile
                profileExists = True
    profileFile.close()

    experienceFile = open("profile_experience.txt", "r")
    for line in experienceFile:
        if line != '\n':
            u, t, e, ds, de, l, d = line.split('\t')
            exp = Experience(u, t, e, ds, de, l, d)
            experienceList.append(exp)
    experienceFile.close()

    educationFile = open("profile_education.txt", "r")
    for line in educationFile:
        if line != '\n':
            u, s, d, y = line.split('\t')
            ed = Education(u, s, d, y)
            educationList.append(ed)
    educationFile.close()

    if profileExists:
        showProfile(userProfile)
    else:
        addProfileTitle(userProfile)
        addProfileMajor(userProfile)
        addProfileUniversity(userProfile)
        addProfileParagraph(userProfile)
        addExperience(username)
        addEducation(username)

    if len(profileList) == 0 or not profileExists:
        profileList.append(userProfile)

    profileFileWrite1 = open("profile.txt", 'w')
    profileFileWrite1.close()


    for profl in profileList:
        profileFileWrite = open("profile.txt", 'a')
        if profl.name == userProfile.name:
            profl = userProfile
        profileFileWrite.write(profl.name + '\t' +
                               profl.title + '\t' +
                               profl.major + '\t' +
                               profl.university + '\t' +
                               profl.about)
        profileFileWrite.close()
       


def showProfile(userProfile):
    cmd = ""
    while (cmd != '0'):
        f = open('profile_experience.txt', 'r+')
        f.truncate(0)

        for expl in experienceList:
            experienceFileWrite = open("profile_experience.txt", 'a')
        
            experienceFileWrite.write(expl.username + '\t' +
                                    expl.title + '\t' +
                                    expl.employer + '\t' +
                                    expl.date_started + '\t' +
                                    expl.date_ended + '\t' +
                                    expl.location + '\t' +
                                    expl.description)
            experienceFileWrite.close()
        
        fn = open('profile_education.txt', 'r+')
        fn.truncate(0)

        for edl in educationList:
            educationFileWrite = open("profile_education.txt", 'a')
        
            educationFileWrite.write(edl.username + '\t' +
                                    edl.school + '\t' +
                                    edl.degree + '\t' +
                                    edl.years + '\n')
            educationFileWrite.close()
        print("")
        print("--------------------")
        print("|    My Profile    |")
        print("--------------------")
        print("")
        print(userProfile.name)
        print("")
        print("Title: " + userProfile.title)
        print("Major: " + userProfile.major)
        print("University: " + userProfile.university)
        print("About Me: " + userProfile.about)

        print("Experience: ")     
        experienceFile = open("profile_experience.txt", "r")
        for line in experienceFile:
            if line != '\n':
                u, t, e, ds, de, l, d = line.split('\t')
                if (u == user):
                    print("Title: " + t)
                    print("Employer: " + e)
                    print("Date started: " + ds)
                    print("Date ended: " + de)
                    print("Location: " + l)
                    print("Description: " + d)
        experienceFile.close()

        print("\nEducation: ")
        educationFile = open("profile_education.txt", "r")
        for line in educationFile:
            if line != '\n':
                u, s, d, y= line.split('\t')
                if (u == user):
                    print("School name: " + s)
                    print("Degree: " + d)
                    print("Year entered: " + y)
        educationFile.close()

        print("")

        print("")
        print("------------------------------")
        print("| '1' to edit title          |")
        print("| '2' to edit major          |")
        print("| '3' to edit university     |")
        print("| '4' to edit about info     |")
        print("| '5' to edit experience     |")
        print("| '6' to edit education      |")
        print("| '0' to return to main page |")
        print("------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            addProfileTitle(userProfile)
        elif (cmd == '2'):
            addProfileMajor(userProfile)
        elif (cmd == '3'):
            addProfileUniversity(userProfile)
        elif (cmd == '4'):
            addProfileParagraph(userProfile)
        elif (cmd == '5'):
            addExperience(user)
        elif (cmd == '6'):
            addEducation(user)
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")


def addProfileTitle(userProfile):
    print("")
    print("***********")
    print("*  Title  *")
    print("***********")
    cmd = input("Add a title or press '0' to return: ")

    if (cmd == '0'):
        return

    userProfile.title = cmd
    return


def addProfileMajor(userProfile):
    print("")
    print("**********")
    print("*  Major *")
    print("**********")
    cmd = input("Add a major or press '0' to return: ")

    if (cmd == '0'):
        return

    major = ""
    majorParse = cmd.split()
    for word in majorParse:
        major += word.capitalize() + " "

    userProfile.major = major
    return

def addProfileUniversity(userProfile):
    print("")
    print("***************")
    print("*  University *")
    print("***************")
    cmd = input("Add a university or press '0' to return: ")

    if (cmd == '0'):
        return

    university = ""
    universityParse = cmd.split()
    for word in universityParse:
        university += word.capitalize() + " "

    userProfile.university = university
    return


def addProfileParagraph(userProfile):
    print("")
    print("**************")
    print("*  About Me  *")
    print("**************")
    cmd = input("Add about info or press '0' to return: ")

    if (cmd == '0'):
        return

    userProfile.about = cmd
    return


def addExperience(username):
    keep_add = "y"
    decision = ""

    while(keep_add == "y" or keep_add == "Y"):

        print("Would you like to add or replace experience?(add/replace) or enter 0 to not add any experience")

        if (decision == "add" or decision == "Add"):
            if (has_max_experience()):
                return
                
            title = input("Enter the title for your job to add: ")
            employer = input("Enter the employer for your job to add: ")
            print("Enter the date you started the job to add: ")
            print("Enter the date ended the job to add: ")
            print("Enter the location for your job to add: ")
            print("Enter the description of what you did to add: ")

            add_experience = Experience(username, title, employer, 101,101,101,101)
            #experienceList.append(add_experience)

            print("-Experience successfully added")

            print("Would you like to add or replace experience?(y/n)")

       
        

        elif (decision == '0'):
            print("No experience ")
            return
        else:
            print("Invalid input")
            return

def has_max_experience():
    user ="Student"
    count = 0
    for line in open("profile_experience.txt", "r"):
         if line != '\n':
            u, t, e, ds, de, l, d = line.split('\t')
            if(u == user):
                count += 1
    if (count == 3):
        print("All permitted experiences have been entered.")
        return True
    return False


def addEducation(username):
    keep_add = "y"
    decision = "add"
    while (keep_add == "y" or keep_add == "Y"):
        print("Would you like to add or replace ducation?(add/replace) or enter 0 to not add education: ")

        if (decision == "add" or decision == "Add"):

            school_name = input("Enter the name of the school to add: ")
            degree = input("Enter the degree to add: ")
            years_attended = input("Enter the year you attended to add: ")

            add_education = Education(username, school_name, degree, years_attended)
            educationList.append(add_education)

            print("Education successfully added")
            
            keep_add = input("Would you like to add or replace more education?(y/n) ")
        elif(decision == "replace" or decision == "Replace"):
            delete_school_name = input("Enter the name of the school to delete: ")
            delete_degree = input("Enter the degree to delete: ")
            delete_years_attended = input("Enter the year you attended to delete: ")
            delete_education = Education(username, delete_school_name, delete_degree, delete_years_attended)
            
            if delete_education not in educationList:
                print("The education entered is not in the list")
                return

            educationList.remove(delete_education)
            print("Education successfully deleted\n")
            school_name = input("Enter the name of the school to add: ")
            degree = input("Enter the degree to add: ")
            years_attended = input("Enter the year you attended to add: ")

            add_education = Education(username, school_name, degree, years_attended)
            educationList.append(add_education)

            print("Education successfully added")
            keep_add = input("Would you like to add or replace more education?(y/n) ")
        
        else:
            count=0
            for edl in educationList:
                if(edl.username == username):
                    count+=1

            if(count == 0):
                print("You must enter at least 1 education")            
            else:
                return
            