import outputApi

def test_my_college_jobs():
    jobs = open("jobs.txt", "r")
    jobList = jobs.readlines()
    jobs.close()
    jobs0 = open("jobs.txt", "w")
    jobs0.write("Student Learner2\tengineering worker\tD\tE\tL\tS\nStudent Learner\tlibrary worker\tA\tB\tC\tD\n")
    jobs0.close()

    outputApi.output_jobs()

    job = open("jobs.txt", "w")
    for line in jobList:
        if line != "\n":
            job.write(line)
    job.close()

    myCollegeJobs = open("MyCollege_jobs.txt", "r").readlines()
    if myCollegeJobs[0] == "Student Learner2\tengineering worker\tD\tE\tL\tS\n":
        if myCollegeJobs[1] == "=====\n":
            if myCollegeJobs[2] == "Student Learner\tlibrary worker\tA\tB\tC\tD\n":
                if myCollegeJobs[3] == "=====\n":
                    assert True
    else:
        assert False
