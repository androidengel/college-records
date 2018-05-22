
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       courserec.py
#Purpose:        class for courserec objects, handling data about a specific term

import course
import student

class courserec():
    def __init__(self, id = None, course = None, professor = None, studentLimit = 0):
        self.recordID = id
        self.course = course
        self.professor = professor
        self.students = []
        self.studentLimit = studentLimit
        
