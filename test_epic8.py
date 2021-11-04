from testHelper import mock_input_output_end,mock_input_output_start,get_output,set_input
import testBase
import notifications

def test_has_not_create_profile_notification():

    #prep the account
    open('accounts.txt', 'w').close()
    file = open("accounts.txt","a")
    file.write("john++ le\n")
    file.close()

    ret = notifications.createProfileNotification("john++ le")

    assert ret == False

def test_numberOfAppliedJobsNotification():
    mock_input_output_start()
    open('appliedJobs.txt', 'w').close()
    name = "john le"
    title = "job"
    g = "2020"
    s = "2021"
    d = "2022"
    dateApplied = "2024"

    testBase.saveJobApp(name, title, g, s, d, dateApplied)
    notifications.numberOfAppliedJobsNotification(name)
    output = get_output()

    assert output == ["",
                    "NOTIFICATION: You have currently applied for 1 jobs",""]
    mock_input_output_end()

def test_checkLastJobAppliedNotification():
    open('appliedJobs.txt', 'w').close()
    name = "john le"
    title = "job"
    g = "2020"
    s = "2021"
    d = "2022"
    dateApplied = "01/01/2024"
    testDate= "01/20/2024"

    testBase.saveJobApp(name, title, g, s, d, dateApplied)
    #false means more than 7 days? 
    assert testBase.checkLastJobAppliedNotification(name,testDate) == True and testBase.checkLastJobAppliedNotification(name,"01/02/2024") == False








    
    
