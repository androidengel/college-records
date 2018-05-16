
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       menu.py
#Purpose:        menu class file


class Menu():
    def __init__(self):
        errorLogin = "Access denied. Incorrect username or password."
        errorCourseFull = "Sorry, this course is not accepting any more students."
    
    def getID(self):
        id = ""
        print("User ID: ")
        return input(id)
        
    def getPassword(self):
        pw = ""
        print("Password: ")
        return input(pw)

    def welcome(self, name):
        print("Access Granted.\nWelcome, {}!".format(name))
        
    def studentMain(self):
        print("Please choose one of the following options:\n",
              "1 - View Student Record\n",
              "2 - View GPA\n",
              "3 - View Courses\n",
              "4 - Enroll in Course\n",
              "0 - Quit")
        choice = ""
        return input(choice)
        
    def studentEnroll(self):
        choice = 0
        print("Please enter the course ID you wish to enroll: ")
        return input(choice)
        
    def facultyMain(self):
        choice = 0
        print("""
            Please choose one of the following options:
            1 - View Course Record
            2 - View Student Record
            3 - Grade Student
            0 - Quit
        """)
        return input(choice)
