from testHelper import mock_input_output_end,mock_input_output_start,get_output,set_input
from testBase import messageNotification
import testBase

#Training option for many things to learn
def test_training_menu():
    mock_input_output_start()

    set_input(["1", "0"])
    training_menu1()

    output = get_output()
    assert output == ['',
'**************',
'*  Training  *',
'**************',
'',
'Welcome to In College Training!',
'-----------------------------------------------------',
"| '1' to go to 'Training and Education'             |",
"| '2' to go to 'IT Help Desk'                       |",
"| '3' to go to 'Business Analysis and Strategy'     |",
 "| '4' to go to 'Security'                           |",
  "| '0' to return to main page                        |",
  '-----------------------------------------------------'
  ]
    mock_input_output_end()

def test_training_training_and_education():
    mock_input_output_start()
    training_menu2()

    set_input(["1"])
    output = get_output()
    assert output == ['',
'**************',
 '*  Training  *',
 '**************',
'',
 'Welcome to In College Training!',
 '-----------------------------------------------------',
 "| '1' to go to 'Training and Education'             |",
 "| '2' to go to 'IT Help Desk'                       |",
 "| '3' to go to 'Business Analysis and Strategy'     |",
  "| '4' to go to 'Security'                           |",
  "| '0' to return to main page                        |",
  '-----------------------------------------------------',
  '',
  '**************************',
  '* Training and Education *',
  '**************************',
 '',
  'Welcome to Training and Education!',
  '-----------------------------------------------------',
 "| '1' to 'Train for an Interview'                   |",
 "| '2' to 'Learn to Make the Perfect Resume'         |",
  "| '3' to 'Sign Up for InCollege Classes'            |",
  "| '4' to 'Test Your Skills'                         |",
  "| '0' to return to main page                        |",
 '-----------------------------------------------------', 
 ]
    mock_input_output_end()

def test_IT_help_desk():
    mock_input_output_start()
    training_menu3()

    set_input(["2"])
    output = get_output()
    assert output == ['',
  '**************',
  '*  Training  *',
  '**************',
  '',
  'Welcome to In College Training!',
  '-----------------------------------------------------',
  "| '1' to go to 'Training and Education'             |",
  "| '2' to go to 'IT Help Desk'                       |",
  "| '3' to go to 'Business Analysis and Strategy'     |",
  "| '4' to go to 'Security'                           |",
  "| '0' to return to main page                        |",
  '-----------------------------------------------------',
  "Coming Soon...press '0' to return to previous menu.",
  ]
    mock_input_output_end()

def test_Buisness_analytics_And_security():
    mock_input_output_start()
    training_menu4()

    set_input(["3"])
    output = get_output()
    assert output == ['',
  '**************',
  '*  Training  *',
  '**************',
  '',
  'Welcome to In College Training!',
  '-----------------------------------------------------',
  "| '1' to go to 'Training and Education'             |",
  "| '2' to go to 'IT Help Desk'                       |",
  "| '3' to go to 'Business Analysis and Strategy'     |",
  "| '4' to go to 'Security'                           |",
  "| '0' to return to main page                        |",
  '-----------------------------------------------------',
  '',
 '*********************',
 '* Business Analysis *',
  '*********************',
  '',
  '-----------------------------------------------------------------',
 "| '1' to learn How to use In College learning                   |",
  "| '2' to learn Train the trainer                                |",
  "| '3' to learn Gamification of learning                         |",
  "| '0' to return to main page                                    |",
 '|                                                               |',
  "| Not seeing what you're looking for?                           |",
  '| Sign in to see all 7,609 results!                             |',
 '-----------------------------------------------------------------',
  ]
    mock_input_output_end()

def test_Security():
    mock_input_output_start()
    training_menu5()

    set_input(["3"])
    output = get_output()
    assert output == ['',
  '**************',
  '*  Training  *',
  '**************',
  '',
  'Welcome to In College Training!',
  '-----------------------------------------------------',
  "| '1' to go to 'Training and Education'             |",
  "| '2' to go to 'IT Help Desk'                       |",
  "| '3' to go to 'Business Analysis and Strategy'     |",
  "| '4' to go to 'Security'                           |",
  "| '0' to return to main page                        |",
  '-----------------------------------------------------',
    "Coming Soon...press '0' to return to previous menu."
  ]
    mock_input_output_end()

def training_menu1():
    cmd = ""
    
    print("")
    print("**************")
    print("*  Training  *")
    print("**************")
    print("")
    print("Welcome to In College Training!")
    print("-----------------------------------------------------")
    print("| '1' to go to 'Training and Education'             |")
    print("| '2' to go to 'IT Help Desk'                       |")
    print("| '3' to go to 'Business Analysis and Strategy'     |")
    print("| '4' to go to 'Security'                           |")
    print("| '0' to return to main page                        |")
    print("-----------------------------------------------------")
   

    
    #TrainingAndEducation()
      
    #comingSoon()
       
    #BusinessAnalysis()
    
    #comingSoon()
    
def training_menu2():
    cmd = ""
    
    print("")
    print("**************")
    print("*  Training  *")
    print("**************")
    print("")
    print("Welcome to In College Training!")
    print("-----------------------------------------------------")
    print("| '1' to go to 'Training and Education'             |")
    print("| '2' to go to 'IT Help Desk'                       |")
    print("| '3' to go to 'Business Analysis and Strategy'     |")
    print("| '4' to go to 'Security'                           |")
    print("| '0' to return to main page                        |")
    print("-----------------------------------------------------")
   

    
    TrainingAndEducation()
      
    #comingSoon()
       
    #BusinessAnalysis()
    
    #comingSoon()

def training_menu3():
    cmd = ""
    
    print("")
    print("**************")
    print("*  Training  *")
    print("**************")
    print("")
    print("Welcome to In College Training!")
    print("-----------------------------------------------------")
    print("| '1' to go to 'Training and Education'             |")
    print("| '2' to go to 'IT Help Desk'                       |")
    print("| '3' to go to 'Business Analysis and Strategy'     |")
    print("| '4' to go to 'Security'                           |")
    print("| '0' to return to main page                        |")
    print("-----------------------------------------------------")
   

    
    #TrainingAndEducation()
      
    comingSoon()
       
    #BusinessAnalysis()
    
    #comingSoon()

def training_menu4():
    cmd = ""
    
    print("")
    print("**************")
    print("*  Training  *")
    print("**************")
    print("")
    print("Welcome to In College Training!")
    print("-----------------------------------------------------")
    print("| '1' to go to 'Training and Education'             |")
    print("| '2' to go to 'IT Help Desk'                       |")
    print("| '3' to go to 'Business Analysis and Strategy'     |")
    print("| '4' to go to 'Security'                           |")
    print("| '0' to return to main page                        |")
    print("-----------------------------------------------------")
   

    
    #TrainingAndEducation()
      
    #comingSoon()
       
    BusinessAnalysis()
    
    #comingSoon()

def training_menu5():
    cmd = ""
    
    print("")
    print("**************")
    print("*  Training  *")
    print("**************")
    print("")
    print("Welcome to In College Training!")
    print("-----------------------------------------------------")
    print("| '1' to go to 'Training and Education'             |")
    print("| '2' to go to 'IT Help Desk'                       |")
    print("| '3' to go to 'Business Analysis and Strategy'     |")
    print("| '4' to go to 'Security'                           |")
    print("| '0' to return to main page                        |")
    print("-----------------------------------------------------")
   

    
    #TrainingAndEducation()
      
    #comingSoon()
       
    #BusinessAnalysis()
    
    comingSoon()

def TrainingAndEducation():
    #cmd = ""
    #while cmd != '0':
        print("")
        print("**************************")
        print("* Training and Education *")
        print("**************************")
        print("")
        print("Welcome to Training and Education!")
        print("-----------------------------------------------------")
        print("| '1' to 'Train for an Interview'                   |")
        print("| '2' to 'Learn to Make the Perfect Resume'         |")
        print("| '3' to 'Sign Up for InCollege Classes'            |")
        print("| '4' to 'Test Your Skills'                         |")
        print("| '0' to return to main page                        |")
        print("-----------------------------------------------------")
        #cmd = input("What would you like to do: ")

        #if (cmd == '1'):
        #    underConstruction()
        #elif (cmd == '2'):
        #    underConstruction()
        #elif (cmd == '3'):
        #    underConstruction()
        #elif (cmd == '4'):
        #    underConstruction()
        #else:
        #    print("Invalid input, please try again")
        #    print("")

    #return


def BusinessAnalysis():
   
   
        print("")
        print("*********************")
        print("* Business Analysis *")
        print("*********************")
        print("")
        print("-----------------------------------------------------------------")
        print("| '1' to learn How to use In College learning                   |")
        print("| '2' to learn Train the trainer                                |")
        print("| '3' to learn Gamification of learning                         |")
        print("| '0' to return to main page                                    |")
        print("|                                                               |")
        print("| Not seeing what you're looking for?                           |")
        print("| Sign in to see all 7,609 results!                             |")
        print("-----------------------------------------------------------------")
        #cmd = input("What would you like to do: ")

        #if (cmd == '1'):
         #   login("")
        #elif (cmd == '2'):
        #    login("")
        #elif (cmd == '3'):
        #    login("")
        #else:
        #    print("Invalid input, please try again")
        #    print("")

   # return


def underConstruction():
    cmd = ""
    while cmd != '0':
        cmd = input("Under Construction...press '0' to return to previous menu.")

def comingSoon():
     print("Coming Soon...press '0' to return to previous menu.")