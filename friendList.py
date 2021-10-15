from profile import Profile
import profile as p1
import profile
from friend import Friend

def showProfile1(userProfile):
    print("")
    print("-------------------------------------")
    print(  userProfile.name + " Profile")
    print("-------------------------------------")
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
            if (u == userProfile):
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
            if (u == userProfile):
                print("School name: " + s)
                print("Degree: " + d)
                print("Year entered: " + y)
    educationFile.close()

    print("-------------------------------------")


def friendList1(username):
    profileExists = False

    friendWithProfileCount = -1
    friendWithProfileMap = {}

    count_friend = -1
    print("-------------------------------------")
    print("| Friend List                       |")
    
    friendFile = open("friendList.txt", "r")
    
    for line in friendFile:
        if line != '\n':
            line = line.rstrip()
            u, fu = line.split('\t')

            if (u == username or fu == username):
                count_friend += 1

                if(u == username):
                    #check if has profile: 
                    profileFile = open("profile.txt", "r")
                    for line in profileFile:
                        if line != '\n':
                            a, t, n, m, p = line.split('\t')
                            profile = Profile(a, t, n, m, p)
                            if (str(profile.name) == str(fu)):
                                profileExists = True
                                friendWithProfileCount +=1

                    profileFile.close()
                    if(profileExists):
                        friendWithProfileMap[friendWithProfileCount] = {fu}
                        print("    Friend name: " + fu + ", "+ str(friendWithProfileCount) +"(has profile)")
                    else: print("    Friend name: " + fu)
                else:
                    #check if friend has profile
                    profileFile = open("profile.txt", "r")
                    for line in profileFile:
                        if line != '\n':
                            a, t, n, m, p = line.split('\t')
                            profile = Profile(a, t, n, m, p)
                            if (str(profile.name) == str(u)):
                                friendWithProfileCount +=1
                                profileExists = True
                    profileFile.close()
                    if(profileExists):
                        friendWithProfileMap[friendWithProfileCount] = {u}
                        print("    Friend name: " + u  + ", "+ str(friendWithProfileCount) +"(has profile)")
                    else: print("    Friend name: " + u)
                
        profileExists = False


    if(count_friend == -1):
        print("| No friend to show                 |")
        print("-------------------------------------")
        friendFile.close() 
    else:
        profileInputSelect = "0"
        
        while( profileInputSelect !=  "-1"):

            profileInputSelect = input("| Enter the coresspond number next to the has profile to see friend profile "
                            + "or enter -1 to exit|")

            profileInputSelect = showProfileOptions_InputValidate1(profileInputSelect)

            if profileInputSelect in friendWithProfileMap:
                profileInputSelect = input("Please put an integer corespond to a has profile selection")
                print("Current profile input: " + profileInputSelect)
            elif profileInputSelect == -1:
                print("exiting...")
            else: 
                profileFile = open("profile.txt", "r")
                for line in profileFile:
                    if line != '\n':
                        u, t, n, m, p = line.split('\t')
                        profile = Profile(u, t, n, m, p)
                        nameToCompare = str(friendWithProfileMap.get(int(profileInputSelect))).replace("{","").replace("}", "").replace("'","")
                        if (profile.name == nameToCompare):
                            userProfile = profile
                            showProfile1(userProfile)
                profileFile.close()

    return_to_main_page = ""
    return_to_main_page = input("Enter exit to return to mainPage")
    while( return_to_main_page != "exit"):
        
        if return_to_main_page == "exit":
            return
        else: 
            return_to_main_page = input("Please enter exit to return to mainPage")

            
            

def showProfileOptions_InputValidate1(userInput):
    while True:
        try:
            int(userInput)
        except ValueError:
            userInput = input("Please input an valid integer options")
            continue
        else:
            return userInput

def test():
    friendFileWrite = open("friendList.txt", 'a')
            
    friendFileWrite.write("Student Learner" + '\t' +
                    "Student2 Learner2" + '\n')
    friendFileWrite.close()

def add_to_friendList():
    friendFile = open("friendList.txt", 'a')
    friendFile.write("Student2 Learner2\tStudent Learner3\n")
    friendFile.write("Student2 Learner2\tStudent Learner4\n")

def set_testprofile():
    profileFile = open("profile.txt",'a')

    student = ["Student Learner3","Student Learner4","Student Learner5","Student Learner6"	]
    profile = "t\tM\tU\ta\n"
    for s in student:
        profileFile.write(s + '\t' + "a" + '\t' + "M"
                    +'\t'+"A" + '\t'+"c"+'\n')



def check_if_has_profile(fu):

    profileFile = open("profile.txt", "r")
    for line in profileFile:
        if line != '\n':
            u, t, n, m, p = line.split('\t')
            profile = Profile(u, t, n, m, p)
            if (profile.name == fu):
                print("there a profile exist for: " + profile.name)
                profileExists = True
            else: print("There's no profile for: " + profile.name
            )
    profileFile.close()
 




