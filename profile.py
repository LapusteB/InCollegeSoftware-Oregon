from re import DOTALL
import csv


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
                               profl.about +'\n')
        profileFileWrite.close()
    
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
                                    expl.description +'\n')
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
                                    expl.description + '\n')
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

        decision = input("Would you like to add or replace experience?(add/replace) or enter 0 to not add any experience")

        if (decision == "add" or decision == "Add"):
            if (has_max_experience()):
                return
                
            title = input("Enter the title for your job to add: ")
            employer = input("Enter the employer for your job to add: ")
            date_started = input("Enter the date you started the job to add: ")
            date_ended = input("Enter the date ended the job to add: ")
            location = input("Enter the location for your job to add: ")
            description = input("Enter the description of what you did to add: ")

            add_experience = Experience(username, title, employer, date_started,date_ended,location,description)
            experienceList.append(add_experience)

            print("-Experience successfully added")

            keep_add = input("Would you like to add or replace experience?(y/n)")

        elif(decision == "replace" or decision == "Replace"):
            delete_title = input("Enter the title for your job you would like to delete: ")
            delete_employer = input("Enter the employer for your job you would like to delete: ")
            delete_date_started = input("Enter the date you started the job you would like to delete: ")
            delete_date_ended = input("Enter the date ended the job you would like to delete: ")
            delete_location = input("Enter the location for your job you would like to delete: ")
            delete_description = input("Enter the description of what you did you would like to delete: ")

            delete_experience = Experience(username, delete_title, delete_employer, delete_date_started,delete_date_ended,delete_location,delete_description)
            
            if delete_experience not in experienceList:
                print("The experience entered is not in the list")
                return

            experienceList.remove(delete_experience)

            print("Experience successfully deleted\n")

            title = input("Enter the title for your job to add: ")
            employer = input("Enter the employer for your job to add: ")
            date_started = input("Enter the date you started the job to add: ")
            date_ended = input("Enter the date ended the job to add: ")
            location = input("Enter the location for your job to add: ")
            description = input("Enter the description of what you did to add: ")

            add_experience = Experience(username, title, employer, date_started,date_ended,location,description)
            experienceList.append(add_experience)
            
            print("Experience successfully added")

            keep_add = input("Would you like to add or replace experience?(y/n)")
        

        elif (decision == '0'):
            print("No experience ")
            return
        else:
            print("Invalid input")
            return

def has_max_experience():
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

    while (keep_add == "y" or keep_add == "Y"):
        decision = input("Would you like to add or replace ducation?(add/replace) or enter 0 to not add education: ")

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
            

            
