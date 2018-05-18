
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       menu.py
#Purpose:        menu class file

import os
import re
import textwrap
import controller
import course

class Menu():
    def __init__(self):
        errorLogin = "Access denied. Incorrect username or password."
        errorCourseFull = "Sorry, this course is not accepting any more students."
    
    def getID(self):
        id = input("User ID: ")
        return id
        
    def getPassword(self):
        pw = input("Password: ")
        return pw

    def welcome(self, name):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Access Granted.\nWelcome, {}!".format(name))
        
    def studentMain(self, id):
        choice = ""
        while choice != '0':
            choice = input(textwrap.dedent("""\
            Please choose one of the following options:
            1 - View My Student Record
            2 - View Courses
            3 - Enroll in Course
            0 - Quit
            """))
            #clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice == '1':
                self.viewStudentRecord(id)
            elif choice == '2':
                self.viewAllCourses()
            elif choice == '3':
                enrollMenu(id)
            elif choice == '0':
                print("Goodbye!")
                return
            else:
                print("Invalid entry.\n")

            input("Press Enter to continue ...")
            #clear console
            os.system('cls' if os.name == 'nt' else 'clear')
        #end while

    def facultyMain(self, id):
        choice = ""
        print("Please choose one of the following options:\n",
              "1 - View A Student Record\n",
              "2 - View My Course Records\n",
              "3 - Edit Course Record\n",
              "0 - Quit")
        return input(choice)

    def viewStudentRecord(self, id):
        record = controller.getStudentData(id)
        print(textwrap.dedent("""\
        STUDENT RECORD
        User ID: {}
        Name: {} {}
        Email: {}
        Date Enrolled: {}
        GPA: {}
        """.format(record[0], record[1], record[2], record[3], record[5], record[6])))

    def viewAllCourses(self):
        courses = controller.getAllCourses()
        print("COURSE OFFERINGS")
        for course in courses:
            print(textwrap.dedent("""\
            Coures ID: {}
            Course Name: {}
            Online: {}
            """.format(course[0], course[1], "Yes" if course[2] == '1' else "No")))
        
    def enrollMenu(self):
        id = "0"
        done = False
        while not done:
            id = input("Please enter the course ID you wish to enroll: ")
            if len(id) != 4:
                print("Invalid course ID.")
                return
            #get course info from db
            data = controller.getCourse(id)
            confirm = input("You selected {}. Are you sure you want to enroll? (Y/N): ".format(data[1]))
            if confirm.lower() == 'y':
                course1 = course.Course(data[0], data[1], data[2])  #create course object

        return input(choice)
