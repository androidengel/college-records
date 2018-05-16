

#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       controller.py
#Purpose:        functions to facilitate messages between main and database

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
        return user1
    else:
        return None

def getStudentData(id):
    if id != "":
        data = db_api.getStudentData(id)
        return data
    else:
        return None

def getCourse(id):
    if id == "":
        return None
    else:
        db_api.getCourse(id)
    