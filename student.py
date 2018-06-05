
#Programmer:     Andrew Engel
#Date created:   2018/05/09
#Filename:       student.py
#Purpose:        student class file

from user import User
import studentrec
import controller
import menu

class Student(User):
    def __init__(self, id, fName, lName, email, pw, enrollment, gpa):
        super().__init__(id, fName, lName, email, pw)
        self.enrollDate = enrollment
        self.GPA = self.calculateGPA()
        
    def calculateGPA(self):
        gpa = controller.calculateGPA(self.id)
        return gpa
                
        