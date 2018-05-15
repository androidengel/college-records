#   Programmer:     Andrew Engel
#   Date created:   2018/05/14
#   Filename:       studentrec.py
#   Purpose:        class for studentrec objects, handling data about a student's school record

import Student
import Course

class StudentRec():
    def __init__(self, recordID = None, student = None):
        self.__recordID = recordID
        self.__student = student
        self.__courses = []
        