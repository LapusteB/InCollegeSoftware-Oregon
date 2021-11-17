from os import close
from os.path import exists
from login import has_max_users

class studentInfo:
    def __init__(self,usrname,fname,lname,password):
        self.usrname = usrname
        self.fname = fname
        self.lname = lname
        self.password = password


def prep_studentAccounts_file():
    print("")
    usrname = "kieu"
    fname = "van"
    lname = "le"
    fullname = "van le"
    password = "P@ssword1"
    
    #a to append, w to over write
    f = open("studentAccounts.txt", "a")
    f.write(usrname +'\t' + fullname + '\n' + password +'\n' + "=====" + '\n')

#prep_studentAccounts_file()
#prep_studentAccounts_file()



def studentAccountAPI():
    path_to_file = "studentAccounts.txt"
    file_exists = exists(path_to_file)
    usrname = ""
    fname = ""
    lname = ""

    studentInfoList = []

    studentCount = 0
    
    if(has_max_users):
        print("Can't create more accounts from studentAccountAPI")
        return
    
    if(exists(path_to_file)):
        print("cool")
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
    
    #put in password file 
    #put in username file
    #put in account file

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
        namesFile.write(student.fname+ student.lname + '\n' )
        passwordsFile.write(student.password)
    
    usernamesFile.close()
    namesFile.close()
    passwordsFile.close()

studentAccountAPI()

def jobsAPI():
    path_to_file = "studentAccounts.txt"
    file_exists = exists(path_to_file)
    return file_exists

#print(studentAccountAPI())


    