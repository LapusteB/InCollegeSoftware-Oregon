from os.path import exists

def has_max_users():
    count = 0
    for line in open("usernames.txt", "r"): count += 1
    if count == 10 or count > 10:
        print("All permitted accounts have been created, please come backlater")
        return True
    return False

class studentInfo:
    def __init__(self,usrname,fname,lname,password):
        self.usrname = usrname
        self.fname = fname
        self.lname = lname
        self.password = password

def prep_studentAccounts_file():
    usrname = "kieu"
    fname = "van"
    lname = "le"
    fullname = "van le"
    password = "P@ssword1"
    
    #a to append, w to over write
    f = open("studentAccounts.txt", "a")
    f.write(usrname +'\t' + fullname + '\n' + password +'\n' + "=====" + '\n')

#---STUDENTACCOUNTAPI---
def studentAccountAPI():
    path_to_file = "studentAccounts.txt"
    usrname = ""
    fname = ""
    lname = ""

    studentInfoList = []
    if(has_max_users()):
        print("System already has 10 users, can't add more from studentAccountsAPI")
        return

    if (exists(path_to_file)):
        f = open("studentAccounts.txt","r")
        for line in f:
            #not empty line 
            if line != '\n':
                #check if usrname and fullname.
                line = line.rstrip()
                if '\t' in line:
                    usrname, fullname = line.split('\t')
                    fname, lname = fullname.split(' ')
                elif '\t' not in line and "=====" not in line:
                    password = line
                    student = studentInfo(usrname,fname,lname,password)
                    studentInfoList.append(student)
        f.close()

    usernamesFile = open("usernames.txt","a")
    namesFile = open("accounts.txt","a")
    passwordsFile = open("passwords.txt","a")

    for student in studentInfoList:
        if(has_max_users()):
            usernamesFile.close()
            namesFile.close()
            passwordsFile.close()
            return

        usernamesFile.write(student.usrname+'\n')
        namesFile.write(student.fname + ' '+student.lname + '\n' )
        passwordsFile.write(student.password + '\n')
    
    usernamesFile.close()
    namesFile.close()
    passwordsFile.close()


class newJobs:
    def __init__(self, title, des, poster, employer, location, salary):
        self.title = title
        self.des  = des 
        self.poster = poster
        self.employer = employer
        self.location = location
        self.salary = salary

def prep_newJobsFile():
    
    title = "job title2"
    description = "job desscription1"
    #the end of multi-line des will be marked by a line
    poster_name = "van le"
    employer_name ="usf"
    location = "tampa"
    salary = "15$/hour"
    f = open("newJobs.txt","a")
    f.write(title + '\n' + description + '\n'+ poster_name + '\n'
            + employer_name + '\n' + location + '\n' + salary + '\n' 
            + "=====\n")

    multiLineDescriptionMarker = "&&&"
    f.close()


def has_max_jobs():
    count = 0
    for line in open("jobs.txt", "r"): count += 1
    if count == 10 or count > 10:
        print("All permitted jobs have been posted(10 jobs), please come back later." + "\n")
        return True
    return False

def saveJob(n, t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(n + "\t" + t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()


def testing():
    f = open("accounts.txt",'r')
    for line in f:
        print(line)

def newJobPosted(username, title):
    file1 = open("accounts.txt", "r")
    file2 = open("newJobPosted.txt", "w")

    for line in file1:
    #line is the username. 

        #poster username not in the accounts database? then add 
        if username not in line:
            line = line.strip('\n')
            file2.write(line + "\t" + title + "\n")
    file1.close()
    file2.close()

#-----NEWJOBSAPI
def newJobsAPI():
    if(has_max_jobs()):
        print("Can't put more jobs from input API!!")
        return

    path_to_file = "newJobs.txt"
    file_exists = exists(path_to_file)

    newJobsList = []
    jobsList = []

    file = open('jobs.txt','r')
    for line in file:
        if line != '\n':
            line = line.rstrip()
            n, t, desscription, emp, loc, sal= line.split('\t')
            jobsList.append(t)
    file.close()
            
    

    if (exists(path_to_file)):
        #open file. 
        f = open("newJobs.txt")
        #split by jobs 
        jobs = f.read().split("=====\n")
        f.close()

        
        #print(jobs)
        #print("separator")

        for job in jobs:
            #f job != '\n' or job != '':
            if job != '':
                if "&&&\n" in job:
                    job.replace("&&&\n","")

                #print(job)
                job = job.rstrip()
                #print(job)
                #print(job)
                title, des, poster, employer, location, salary= job.split('\n')
                #title,des = job.split('\n')
                #thesplit = job.split("\n")
                #print(thesplit)

                jobObj = newJobs(title, des, poster, employer, location, salary)
                newJobsList.append(jobObj)

    #saveJobs 
    for job in newJobsList:
        if(has_max_jobs()):
            return
        if job.title not in jobsList:
            saveJob(job.poster, job.title, job.des, job.employer, job.location, job.salary)
            newJobPosted(job.poster, job.title)
    
    

            #not empty line 
            # if line != '\n':
            #     #check if usrname and fullname.
            #     line = line.rstrip()
            #     if lineCount == 0:
            #         title = line
            #     elif lineCount == 1:
            #         des = line 
            #     elif lineCount == 2 and line != "&&&":
            #         poster = line 
            #     elif lineCount == 2 and line == "&&&":

                
                
            #         f.close()

#----TRAININGAPI
def trainingAPI():
    path_to_file = "newtraining.txt"

    #newtrainingList = []
    if(exists(path_to_file)):
        f = open("newtraining.txt",'r')
        f2 = open("training.txt","a")
        for line in f:
            line = line.rstrip()
            f2.write(line + '\n')
            #ewtrainingList.append(line)
        
        f.close()
        f2.close()
    else:
        return

#APPLIEDJOBSAPI (3 FUNCTIONS)
def apply_appliedJobsAPI(title, applicant, des):

    #get name
    f1 = open('accounts.txt','r')
    accounts = f1.readlines()
    f1.close()
    #get username

    usernameList = []
    
    f2 = open('usernames.txt','r')
    usernames = f2.readlines()
    for username in usernames:
        usernameList.append(username.rstrip())
    f2.close()

    index = accounts.index(applicant + '\n')


    file = open("MyCollege_appliedJobs.txt","a")
    file.write(title + '\t' + usernameList[index] + '\t' + des + '\n' + "=====\n")
    file.close()

def post_appliedJobsAPI(title):
    file = open("MyCollege_appliedJobs.txt","a")
    file.write(title + '\n' + "=====\n")
    file.close()

def delete_appliedJobsAPI(title):

    newer_appliedJobsList = []
    file = open("MyCollege_appliedJobs.txt")
    jobs = file.read().split("=====\n")
    file.close()
    #print(jobs)

    

    #job in mycollege: 
    for job in jobs:
        #if delete title not in job then append to list.
        if job != '':
            if (title + '\t') not in job and (title + '\n') not in job:
                job = job + "=====\n"
                newer_appliedJobsList.append(job)
    #clear old file
    open('MyCollege_appliedJobs.txt', 'w').close()

    file = open("MyCollege_appliedJobs.txt","a")

    #write new jobs in
    for job in newer_appliedJobsList:
        file.write(job)
    file.close()

#apply_appliedJobsAPI('title4',"john++ le",'des')
#post_appliedJobsAPI('title3')
#delete_appliedJobsAPI('title3')

    
        


#trainingAPI()




#prep_newJobsFile()
#prep_newJobsFile()

#jobsAPI()



#prep_newJobsFile()
#prep_newJobsFile()


#prep_studentAccounts_file()
#prep_studentAccounts_file()
#studentAccountAPI()
#print(studentAccountAPI())

#apply_appliedJobsAPI('title',"john++ le",'des')



    