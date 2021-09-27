from os import name

def jobSearchPage():
    print("\n")
    print("Job Search")
    print("------------")
    a = input("Press '0' to return or 1 to post a new job.")

    if a == "0":
        print("mainPage")
        #mainPage(name)
    elif(a == "1"):
        postNewJob()

def mainPage2(nameofuser):
    global name
    name = nameofuser

    kbInput = "-1"

    while(kbInput != "1" and kbInput != "2" and kbInput != "3"):
        print("")
        print("--------------------------------------------------------")
        print("InCollege")
        print("--------------------------------------------------------")
        print("Main page")
        print(" Enter page you want to go to: ")
        kbInput = input("   '1' to find someone you know, '2' for learn new skills, '3' for job search/ internship, '0' to return to login\n")
        if(kbInput == "1"):
            #peopleSearchPage()
            print("")
        elif(kbInput == "2"):
            #skillsPage()
            print("")
        elif(kbInput == "3"):
            jobSearchPage()
            print("")
        elif(kbInput == "0"):
            from Users import home
            home('')
        else:
            print("Please enter an available option!!\n")


def mainPage(nameofuser):
    global name
    name = nameofuser

    kbInput = "-1"

    while(kbInput != "1" and kbInput != "2" and kbInput != "3" and kbInput != "4"):
        print("")
        print("--------------------------------------------------------")
        print("InCollege")
        print("--------------------------------------------------------")
        print("Main page")
        print(" Enter page you want to go to: ")
        kbInput = input("   '1' to find someone you know, '2' for learn new skills, '3' for search for job, '4' to post a new job, '0' to return to login\n")
        if(kbInput == "1"):
            print("")
            #peopleSearchPage()
        elif(kbInput == "2"):
            print("")
            #skillsPage()
        elif(kbInput == "3"):
            #print("")
            jobSearchPage()
        elif(kbInput == "4"):
            postNewJob()
        elif(kbInput == "0"):
            from Users import home
            home('')
        else:
            print("Please enter an available option!!\n")


def postNewJob():
    select = "x"
    print("-----------------------------------")
    print(" Welcome to the Job Creation Page! ")
    print("-----------------------------------")
    while(select != 'y' and select != 'Y' and select != 'n' and select != "N"):
        select = input("Would you like to create a job? ('y' or 'n'): ")
        if (select == 'y' or select =='Y'):
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
    #mainPage(name)


def saveJob(n, t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(n + "\t" + t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()