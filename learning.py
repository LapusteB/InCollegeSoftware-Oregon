#from Users import output_training

def learningMenu(name):
    cmd = ''
    while(cmd!='0'):
        print("Welcome to In College Learning\n")
        print("")
        print("-----------------------------------------------------------------")
        print("| '1' to learn How to use In College learning                   |")
        print("| '2' to learn Train the trainer                                |")
        print("| '3' to learn Gamification of learning                         |")
        print("| '4' to learn Understanding the Architectural desing Process   |")
        print("| '5' to learn Project Management Simplified                    |")
        print("| '0' to return to main page                                    |")
        print("-----------------------------------------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            InCollegeLearning(name)
        elif (cmd == '2'):
            Train(name)
        elif (cmd == '3'):
            Gamification(name)
        elif (cmd == '4'):
            Understanding(name)
        elif (cmd == '5'):
            Project(name)
        elif (cmd == '0'):
            continue
        else:
            print("Invalid input, please try again")
            print("")
    return

def InCollegeLearning(name):
    if(taken_Incollege(name)):
        decision = input("You have already taken this course, do you want to take it again? (y/n)\n")
        if(decision == 'y'):
            print("You have now completed this training\n")
        elif(decision == 'n'):
            print("Course Cancelled\n")
        else:
            print("Please enter valid input\n")

    else:
        learningfile = open("learning.txt", 'a')
        learningfile.write(name + '\t' + "How to use In College learning" + '\n')
        learningfile.close()    
        output_training()
        print("You have now completed this training")

def taken_Incollege(name):
    
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')
            
            if(u == name and i == "How to use In College learning" + '\n'):
                return True
    return False

def Train(name):
    if(taken_Train(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        if(decision == 'y'):
            print("You have now completed this training\n")
        elif(decision == 'n'):
            print("Course Cancelled\n")
        else:
            print("Please enter valid input\n")
    else:
        learningfile = open("learning.txt", 'a')
        learningfile.write(name + '\t' + "Train the trainer" + '\n')
        learningfile.close()  
        output_training()
        print("You have now completed this training")

def taken_Train(name):
    
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')
            
            if(u == name and i == "Train the trainer" + '\n'):
                return True
    return False

def Gamification(name):
    if(taken_Gamification(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        if(decision == 'y'):
            print("You have now completed this training\n")
        elif(decision == 'n'):
            print("Course Cancelled\n")
        else:
            print("Please enter valid input\n")
    else:
        learningfile = open("learning.txt", 'a')
        learningfile.write(name + '\t' + "Gamification of learning" + '\n')
        learningfile.close() 
        output_training() 
        print("You have now completed this training")

def taken_Gamification(name):
    
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')
            
            if(u == name and i == "Gamification of learning" + '\n'):
                return True
    return False

def Understanding(name):
    if(taken_Understanding(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        if(decision == 'y'):
            print("You have now completed this training\n")
        elif(decision == 'n'):
            print("Course Cancelled\n")
        else:
            print("Please enter valid input\n")
    else:
        learningfile = open("learning.txt", 'a')
        learningfile.write(name + '\t' + "Understanding the Architectural desing Process" + '\n')
        learningfile.close()
        output_training()
        print("You have now completed this training")

def taken_Understanding(name):
    
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')
            
            if(u == name and i == "Understanding the Architectural desing Process" + '\n'):
                return True
    return False

def Project(name):
    if(taken_Project(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        if(decision == 'y'):
            print("You have now completed this training\n")
        elif(decision == 'n'):
            print("Course Cancelled\n")
        else:
            print("Please enter valid input\n")
    else:
        learningfile = open("learning.txt", 'a')
        learningfile.write(name + '\t' + "Project Management Simplified" + '\n')
        learningfile.close()
        output_training()
        print("You have now completed this training")

def taken_Project(name):
    
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')
            
            if(u == name and i == "Project Management Simplified" + '\n'):
                return True
    return False


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