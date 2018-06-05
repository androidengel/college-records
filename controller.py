

#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       controller.py
#Purpose:        functions to facilitate communiation to and from the database

import user
import student
import faculty
import course
import db_api

def createDB():
    db_api.createDB()
    
def authenticate(id, pw):
    if id != "" or pw != "":
        user1 = db_api.authenticate(id, pw)
        return user1    #returns user record from DB
    else:
        return None

def getStudentData(id):
    if id != "":
        data = db_api.getStudentData(id)
        return data
    else:
        return None

def getFacultyData(id):
    if id != "":
        data = db_api.getFacultyData(id)
        return data
    else:
        return None

def getCourse(id):
    if id == "":
        return None
    else:
        return db_api.getCourse(id)

def getAllCourses():
    courses = db_api.getAllCourses()
    return courses

def getStudentCourses(studentID):
    if studentID == "":
        return None
    else:
        return db_api.getStudentCourses(studentID)

def numStudentsInCourse(courseid):
    if courseid == "":
        return None
    else:
        return db_api.numStudentsInCourse(courseid)

def enroll(studentid, courseid):
    if studentid == "" or courseid == "":
        return None
    else:
        db_api.enroll(studentid, courseid)

def getCourseRecords(userID):
    return db_api.getCourseRecords(userID)

def getStudentID(userID):
    return db_api.getStudentID(userID)

def gradeStudent(courseID, facultyID, studentID, grade):
    if courseID == "" or facultyID == "" or studentID == "" or grade == "":
        return
    else:
        db_api.gradeStudent(courseID, facultyID, studentID, grade)
        calculateGPA(studentID)

def isEnrolled(studentID, courseID):
    if studentID == "" or courseID == "":
        return
    else:
        return db_api.isEnrolled(studentID, courseID)

def calculateGPA(studentID):
    gpa_dict = {93 : 4.0, 90 : 3.7, 87 : 3.3, 80 : 2.7, 77 : 2.3, 73 : 2.0, 70 : 1.7, 76 : 1.3, 65 : 1.0, 0 : 0.0 }
    grades = getStudentGrades(studentID)

    #determine gpa for each course and add to courseGPAs list
    courseGPAs = []
    for grade in grades:
        g = grade[0]
        for key in sorted(gpa_dict.keys(), reverse = True):
            if g >= key:
                courseGPAs.append(gpa_dict[key])
                break
    #sum courseGPAs together and divide by number of courseGPAs
    sumGPA = 0.0
    for course_gpa in courseGPAs:
        sumGPA += course_gpa
    #validate non-zero divisor and calculate GPA
    gpa = 0.0
    if sumGPA > 0.0:
        gpa = sumGPA / len(courseGPAs)
    #update GPA in student table
    db_api.updateStudentGPA(studentID, gpa)
    return gpa


def getStudentGrades(studentID):
    return db_api.getStudentGrades(studentID)

#**************TESTING FUNCTIONS***************

def getAllStudentRecords():
    return db_api.getAllStudentRecords()

def getAllCourseRecords():
    return db_api.getAllCourseRecords()