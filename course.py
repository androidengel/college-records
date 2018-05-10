"""
    Programmer:     Andrew Engel
    Date created:   2018/05/09
    Filename:       course.py
    Purpose:        course class file
"""

from faculty import Faculty

class Course():
    def __init__(self):
        self.ID = 0
        self.name = ""
        self.professor = Faculty()
        