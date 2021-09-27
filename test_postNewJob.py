
from testBase import mock_input_output_start, mock_input_output_end, postNewJob, set_input, get_output
import testBase2
from os import name
import re

#EMPTY JOBS.TXT FILE BEFORE TESTING
input_values = []
print_values = []

def test_post_job():
    print("")
    mock_input_output_start()
    set_input(["3","1","y","a","a","a","a","a",
                "3","1","y","a","a","a","a","a"])
    

    testBase2.mainPage2("van le")
    testBase2.mainPage2("kieu le")
    file = open("jobs.txt","r")
    contents = file.readlines()
    file.close()
    open('jobs.txt', 'w').close()

    a = re.sub("^(\\S*\\s+\\S+).*", "\\1", contents[0])
    b = re.sub("^(\\S*\\s+\\S+).*", "\\1", contents[1])
    
    
    assert a == "van le\n" and b == "kieu le\n"
    mock_input_output_end()



def test_post_passed_5_jobs():
    mock_input_output_start()
    set_input(["y","a","a","a","a","a",
    "y","a","a","a","a","a",
    "y","a","a","a","a","a",
    "y","a","a","a","a","a",
    "y","a","a","a","a","a","y"
                ])

    
                
    postNewJob()
    postNewJob()
    postNewJob()
    postNewJob()
    postNewJob()

    
    output = get_output()
    assert output == ["-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): ",""
                ,"Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: "

                 ,"-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): ",""
                ,"Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: "
                 
                 ,"-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): ",""
                ,"Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: "
                 
                 ,"-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): ",""
                ,"Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: "
                 
                 ,"-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): ",""
                ,"Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: "]

    mock_input_output_end()

