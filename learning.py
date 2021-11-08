def learningMenu(name):

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
        return
    else:
        print("Invalid input, please try again")
        print("")

def InCollegeLearning(name):
    if(taken_Incollege(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        
    else:
        print("You have now completed this training")

def taken_Incollege(name):
    
    for line in open("learning.txt", "r"):
        if line != '\n':
            u, i = line.split('\t')
            
            if(u == name and i == "How to use In College learning" + '\n'):
                return True
    return False

def Train(name):
    if(taken_Incollege(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        
    else:
        print("You have now completed this training")

def Gamification(name):
    if(taken_Incollege(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        
    else:
        print("You have now completed this training")

def Understanding(name):
    if(taken_Incollege(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        
    else:
        print("You have now completed this training")

def Project(name):
    if(taken_Incollege(name)):
        decision = input("You have already taken this course, do you want to take it again?\n")
        
    else:
        print("You have now completed this training")