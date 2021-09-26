
from testBase import createNewJob, has_max_jobs, mock_input_output_start, mock_input_output_end, postNewJob, set_input, get_output


input_values = []
print_values = []

#why the code broke at 4 though?
def test_post_passed_5_jobs():
    mock_input_output_start()
    set_input(["y","a","a","a","a","a",
    "y","a","a","a","a","a",
    "y","a","a","a","a","a",
    "y","a","a","a","a","a",
    "y","a","a","a","a","a","y"
                ])

    '''
    "y","a","a","a","a","a",
                "y","a","a","a","a","a",
                "y","a","a","a","a","a",
                "y","a","a","a","a","a",
                ])
    '''
                
    postNewJob()
    postNewJob()
    postNewJob()
    postNewJob()
    postNewJob()
    #postNewJob()
    '''
    postNewJob()
    postNewJob()
    postNewJob()
    postNewJob()
    '''
    
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
                 
'''

                 "-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): ",
                "All permitted jobs have been posted, please come back later." + "\n", "max jobs 5"]
                '''

    #mock_input_output_end()

'''

 "-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): "
                "","Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: ",
                 "-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): "
                "","Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: ",
                 "-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): "
                "","Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: ",
                 "-----------------------------------"," Welcome to the Job Creation Page! ",
                "-----------------------------------","Would you like to create a job? ('y' or 'n'): "
                "","Enter the title for your job: ","Enter the description for your job: ","Enter the employer for your job: ",
                 "Enter the location for your job: ", "Enter the salary for your job: "]
'''



#how is it though;  i do not know at all though 
#this is weird though; but i like the theme 

