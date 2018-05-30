

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

def getCourseRecords(facultyID):
    return db_api.getCourseRecords(facultyID)

def gradeStudent(courseID, facultyID, studentID, grade):
    if courseID == "" or facultyID == "" or studentID == "" or grade == "":
        return
    else:
        db_api.gradeStudent(courseID, facultyID, studentID, grade)

#**************TESTING FUNCTIONS***************

def getAllStudentRecords():
    return db_api.getAllStudentRecords()

def getAllCourseRecords():
    return db_api.getAllCourseRecords()