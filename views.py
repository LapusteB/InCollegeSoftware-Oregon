from os import name
import usefulLinks
import profile
import friend
import friendList

savedJobsMap = {}
savedJobsList = []
savedJobsListObj = []
jobList = []
appliedJobsList = []
unmarkJobsMap = {}
countJob = 0

class savedJob:
    def __init__(self, studentName, title):
        self.studentName = studentName
        self.title = title
    
    def __eq__(self,other):
        return self.studentName == other.studentName and self.title == other.title


def mainPage(nameofuser):
    global name
    name = nameofuser

    friend.has_pending_requests(nameofuser)
    
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
        print("| '6' to show your network          |")
        print("| '7' to show your friendList       |")
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
        elif (kbInput == '6'):
            friend.friendMenu(name)
        elif (kbInput == '7'):
            friendList.friendList1(name)
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
    if count == 10 or count > 10:
        print("All permitted jobs have been posted(10 jobs), please come back later." + "\n")
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

def update_jobs_appliedJobs_and_savedJobs():

    jobList.clear()

    jobFile = open("jobs.txt",'r')
    for line in jobFile:
        if line != '\n':
            line = line.rstrip()
            n, t, d, e, l, s = line.split('\t')
            jobList.append(t)

    jobFile.close()

    #saved the applied jobs 

    appliedJobsList.clear()

    appliedJobsFile = open("appliedJobs.txt",'r')
    for line in appliedJobsFile:
        if line != '\n':
            line = line.rstrip()
            n, t, start, end, des = line.split('\t')
            if(n == name):
                appliedJobsList.append(t)

    appliedJobsFile.close()

    #open the applied jobs 

    savedJobsListObj.clear()
    savedJobsList.clear()
    file = open("savedJobs.txt",'r')
    for line in file:
        if line != '\n':
            line = line.rstrip()
            n, t = line.split('\t')
            if(n == name):
                savedJobsObj = savedJob(name,t)
                savedJobsListObj.append(savedJobsObj)
                savedJobsList.append(t)

    file.close()

def update_after_savedJobsFile_change():
    print("")

    #open the applied jobs 
    file = open("savedJobs.txt",'r')
    for line in file:
        if line != '\n':
            line = line.rstrip()
            n, t = line.split('\t')
            if(n == name):
                savedJobsObj = savedJob(name,t)
                savedJobsListObj.append(savedJobsObj)
                savedJobsList.append(t)

    file.close()

def printJob():
    global countJob
    countJob = 0
    
    for i in range(len(jobList)):      
        if jobList[i] in appliedJobsList:
            if jobList[i] in savedJobsList:
                countJob +=1
                savedJobsMap[int(countJob)] = {jobList[i]}
                print( str(countJob) + ". "+ jobList[i] + " (applied),(saved)")
            else: 
                countJob +=1
                unmarkJobsMap[int(countJob)] = {jobList[i]}
                print( str(countJob) + ". "+ jobList[i] + " (applied)")
        else:
            if jobList[i] in savedJobsList:
                countJob +=1
                savedJobsMap[int(countJob)] = {jobList[i]}
                print( str(countJob) + ". "+ jobList[i] + " (saved)")
            else: 
                countJob +=1
                unmarkJobsMap[int(countJob)] = {jobList[i]}
                print( str(countJob) + ". "+ jobList[i])
    



def jobSearchPage():
    global countJob

    print("\n")
    print("Job Search/ Internship")
    print("------------------------------------")

    check_if_applied_jobs_got_deleted()


    #saved all the jobs
    #refresh the jobs
    update_jobs_appliedJobs_and_savedJobs()
    
    if len(jobList) >= 1:
        print("List of all jobs")
    else: print("No job has been posted")

    printJob()
    b = "x"

    #saved jobs and unmark jobs options
    while( b != "-1"):
        b = input("Enter 'a' to appy for jobs, Enter 's' to save jobs, 'u' to unmark a job or " + 
        "enter -1 to to see more options: ")
        if b == "s":

            c = "x"
            while c != "-1":
            
                c = input("Enter the number coresspond to the job to save or -1 to exit: ")
                if c == "-1":
                    break

                if int(c) in savedJobsMap or int(c) > len(savedJobsList) + 1:
                    print("Please enter a number corespond to a unmarks job to save" +
                    " or '-1' to exit saving")
                else: 
                    #saved jobs 

                    #get the saved jobs from the map. 

                    #create an obj
                    jobTitle = str(unmarkJobsMap.get(int(c))).strip('{').strip('}').strip("'").rstrip()
                    savedJobsObj1 = savedJob(name, jobTitle)
                    
                    #put in the saved maps
                    savedJobsMap[int(c)] = {jobTitle}
                    del unmarkJobsMap[int(c)]
                    
                    savedJobsListObj.append(savedJobsObj1)
                    savedJobsList.append(jobTitle)
                    

                    #change the .txt file 
                    f = open('savedJobs.txt', 'r+')
                    f.truncate(0)
                    f.close()

                    file = open("savedJobs.txt", 'a')
                    for obj in savedJobsListObj:
                        file.write(obj.studentName + "\t" + obj.title + "\n")
                    
                    file.close()
                    print("Job saved!!!")
                    #update_jobs_appliedJobs_and_savedJobs()
                    printJob()
        elif b =="a":
            j=0
            
            while(j!=1):
                sel = input("Enter the name of the job you want to apply to: ")    
                if (sel in jobList):
                    jobApplication(sel)
                    j=1


        elif b == "u":
            c = "x"
            while c != "-1":

                c = input("Enter the number coresspond to the job to unmark or -1 to exit unmarking: ")
                if c == "-1":
                    break
                if int(c) not in savedJobsMap:
                    print("Please enter a number corespond to a unmarks job to save" +
                    " or '-1' to exit")

                #it is in the map
                else: 
                    #unmark 
                    #remove the job by del in the obj list
                    for job in savedJobsListObj:
                        jobTitle = str(savedJobsMap.get(int(c))).strip('{').strip('}').strip("'").rstrip()

                        if job.studentName == name and job.title == jobTitle:

                            #remove from saved list
                            savedJobsList.remove(job.title)

                            #remove from saved maps
                            del savedJobsMap[int(c)]
                            #append to unmark map: 
                            unmarkJobsMap[int(c)] = {job.title}
                            unmark_savedJobsObj2 = savedJob(name, job.title)
                            savedJobsListObj.remove(unmark_savedJobsObj2)
                    
                    #clear the txt old file
                    f = open('savedJobs.txt', 'r+')
                    f.truncate(0)
                    f.close()

                    file = open("savedJobs.txt", 'a')
                    #write in new data for saveJobsList
                    for obj in savedJobsListObj:
                        file.write(obj.studentName + "\t" + obj.title + "\n")
                        
                    file.close()
                    print("Job unmarked!!!")

                    #some not necessary though. 
                    printJob()
                    #this change the saveJobsMap and unmark though: 

    a = "x"

    #generate list of appliedJobs and savedJobs and not yet applied jobs.
    print("------------------------------------")

    while (a != "0" and a != "1" and a != "2" and a != "3"):
        a = input("Press '0' to return to mainPage," +
        " '1' to post a new job, '2' to generate list of jobs applied, "
        + "'3' to generate list of saved jobs or " + 
        " '4' to generate list of jobs that you have not applied yet: ")
        if a == "0":
            mainPage(name)
            #return
        elif (a == "1"):
            postNewJob()
        elif (a == "2"):
            appliedJobListGenerate()
        elif (a == "3"):
            savedJobListGenerate()
        elif (a == "4"):
            notAppliedJobsListGenerator()
        else:
            print("Please enter an available option!!\n")

def jobApplication(title):

    print("----------JOB APPLICATION----------")
  
    g = input("Enter your graduation date Ex:(mm/dd/yyyy): ")
    s = input("Enter the day you can start Ex:(mm/dd/yyyy): ")
    d = input("Describe why you feel fit for the job: ")
    
    saveJobApp(name, title, g, s, d)
    

def saveJobApp(name, title, g, s, d):
    file5 = open("appliedJobs.txt", "a")
    file5.write(name + "\t" + title + +"\t" + g + "\t" + s + "\t" + d + "\n" )
    file5.close()
    

def job_got_deleted_notification(jobName):
    appliedJobsGotDeletedFile = open("appliedJobsDeleted.py",'a')
    appliedJobsGotDeletedFile.write(name + '\t' + jobName +'\n')
    appliedJobsGotDeletedFile.close()


#check if applied jobs got deleted
def check_if_applied_jobs_got_deleted():
    deletedJobsList = []
    deletedJobsObjList = []

    #the file got student name and job name; 
    #if the student name and job name match then
    appliedJobsGotDeletedFile = open("appliedJobsDeleted.txt",'r')
    for line in appliedJobsGotDeletedFile:
        if line != '\n':
            #n for student name and t for job title
            line = line.rstrip()
            n,t = line.split('\t')
            
            if(n == name):
                deletedJobsList.append(t)
            else: 
                other_user_applied_jobs_deleted = savedJob(n,t)
                deletedJobsObjList.append(other_user_applied_jobs_deleted)
    
    appliedJobsGotDeletedFile.close()

    f = open("appliedJobsDeleted.txt", 'r+')
    f.truncate(0)
    f.close()

    #put back other user deleted jobs
    file = open("appliedJobsDeleted.txt", 'a')
    for obj in deletedJobsObjList:
        file.write(obj.studentName + "\t" + obj.title + "\n")
    file.close()

    appliedJobsGotDeletedFile.close()


    #print("list length: " + str(len(deletedJobsList)))
    if len(deletedJobsList) >= 1:
        print("Here are the job(s) You've applied for has(have) been deleted:")
        print(*deletedJobsList,sep =', ')
            
            
        print("------------------------------------")


def appliedJobListGenerate():
    
    appliedJobsList = []
    #open the applied jobs 
    file = open("appliedJobs.txt",'r')
    for line in file:
        if line != '\n':
            line = line.rstrip()
            n, t, start, end, des = line.split('\t')
            if(n == name):
                appliedJobsList.append(t)

    file.close()

    print("List of applied jobs:")
    print(*appliedJobsList, sep = ', ')

    a = "x"
    while a != "0":
        a = input("Enter '0' to return to job search/ internship page")
        if a != "0":
            print("Please enter '0' to return")
        else: jobSearchPage()
    
    print("------------------------------------")

def notAppliedJobsListGenerator():
    appliedJobsList = []
    jobList = []

    #open the applied jobs 
    file = open("appliedJobs.txt",'r')
    for line in file:
        if line != '\n':
            line = line.rstrip()
            n, t, start, end, des = line.split('\t')
            if(n == name):
                appliedJobsList.append(t)

    file.close()

    jobFile = open("jobs.txt",'r')
    for line in jobFile:
        if line != '\n':
            line = line.rstrip()
            n, t, d, e, l, s = line.split('\t')
            jobList.append(t)

    jobFile.close()

    print("List of jobs that has been applied to:")
    for i in range(len(appliedJobsList)): 
        if appliedJobsList[i] in jobList:
            print(str(appliedJobsList[i]))

    a = "x"
    while a != "0":
        a = input("Enter '0' to return to job search/ internship page")
        if a != "0":
            print("Please enter '0' to return")
        else: jobSearchPage()
    
    print("------------------------------------")


def savedJobListGenerate():
    savedJobsList = []
    #open the applied jobs 
    file = open("savedJobs.txt",'r')
    for line in file:
        if line != '\n':
            line = line.rstrip()
            n, t = line.split('\t')
            if(n == name):
                savedJobsList.append(t)

    file.close()
    
    print("List of saved jobs:")
    print(*savedJobsList, sep = ', ')

    a = "x"
    while a != "0":
        a = input("Enter '0' to return to job search/ internship page")
        if a != "0":
            print("Please enter '0' to return")
        else: jobSearchPage()
    
    print("------------------------------------")
    

def pageUnderConstruction():
    print("")
    print("--------------------------------------------------------")
    print("Page under construction")








