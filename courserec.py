#   Programmer:     Andrew Engel
#   Date created:   2018/05/14
#   Filename:       courserec.py
#   Purpose:        class for courserec objects, handling data about a specific term

import Course
import Student

class courserec():
    def __init__(self, id = None, course = None, professor = None, studentLimit = 0):
        self.__recordID = id
        self.__course = course
        self.__professor = professor
        self.__students = []
        self.__studentLimit = studentLimit
        