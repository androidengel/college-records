
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       menu.py
#Purpose:        menu class file

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
        print("Access Granted.\nWelcome, {}!".format(name))
        
    def studentMain(self, id):
        choice = input(textwrap.dedent("""\
        Please choose one of the following options:
        1 - View My Student Record
        2 - View Courses
        3 - Enroll in Course
        0 - Quit
        """))
        return choice

    def facultyMain(self, id):
        choice = input(textwrap.dedent("""\
        Please choose one of the following options:
        1 - View A Student Record
        2 - View My Course Records
        3 - Grade Student
        0 - Quit
        """))
        return choice

    def viewCourseRecords(self, userID):
        records = controller.getCourseRecords(userID)
        #create list of unique course IDs to ensure all students are being printed before moving to next course
        courseIDs = []
        if records:     #if list is not empty
            print("YOUR COURSE RECORDS", end="")
            for record in records:
                if record[0] not in courseIDs:
                    print(f"\nCourse ID: {record[0]}\nCourse Name: {record[1]}\nStudents:")
                    courseIDs.append(record[0])
                print(f"  {record[2]} {record[3]}")
        else:
            print("No course records found.")


    def facViewStudentRecord(self):
        choice = input("Please enter a student's user ID to view their record: ")
        if len(choice) != 6:
            print("Invalid student user ID.")
            return
        record = controller.getStudentData(choice.lower())
        if record == None or record[7].lower() != 'student':
            print("Student not found")
        else:
            self.viewStudentRecord(choice.lower())

    def viewStudentRecord(self, id):
        record = controller.getStudentData(id)
        gpa = controller.calculateGPA(record[8])
        courses = controller.getStudentCourses(id)
        print(textwrap.dedent("""\
        STUDENT RECORD
        User ID: {}
        Name: {} {}
        Email: {}
        Date Enrolled: {}
        GPA: {}
        """.format(record[0], record[1], record[2], record[3], record[5], gpa)))
        for crse in courses:
            print("Course ID: {}\nCourse Name: {}\nOnline: {}".format(crse[0], crse[1], "Yes" if crse[2] == 1 else "No"))

    def gradeStudent(self, facultyID):
        valid = False
        while not valid:
            userID = input("Please enter the student's user ID: ")
            if len(userID) == 6:
                stID = controller.getStudentID(userID)
                valid = True
            else:
                print("Invalid user ID.")

        valid = False
        while not valid:
            crsID = input("Please enter the course ID: ")
            if len(crsID) == 4:
                valid = True
            else:
                print("Invalid course ID.")

        valid = False
        while not valid:
            grade = input("Please enter the student's grade: ")
            grade = float(grade)
            if grade >= 0 and grade <= 100:
                controller.gradeStudent(crsID, facultyID, stID, grade)
                valid = True
            else:
                print("Invalid grade.")


    def viewAllCourses(self):
        courses = controller.getAllCourses()
        print("COURSE OFFERINGS")
        for course in courses:
            print(textwrap.dedent("""\
            Coures ID: {}
            Course Name: {}
            Online: {}
            """.format(course[0], course[1], "Yes" if course[2] == 1 else "No")))
        
    def enrollMenu(self):
        done = False
        while not done:
            id = input("Please enter the course ID you wish to enroll: ")
            if len(id) != 4:
                print("Invalid course ID.")
                return
            #get course info from db
            data = controller.getCourse(id)
            if data != None:
                confirm = input("You selected {}. Are you sure you want to enroll? (Y/N): ".format(data[1]))
                if confirm.lower() == 'y':
                    course1 = course.Course(data[0], data[1], data[2])  #create course object
                    done = True
                    return course1
                else:
                    print("Enrollment aborted.")
            else:
                print("Course not found.")
