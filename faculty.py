
#Programmer:     Andrew Engel
#Date created:   2018/05/09
#Filename:       faculty.py
#Purpose:        faculty class file

from user import User
import menu
import studentrec
import courserec

class Faculty(User):
    def __init__(self, id, fName, lName, email, pw, hireDate):
        super().__init__(id, fName, lName, email, pw)
        self.hireDate = hireDate

    def login(self, mnu):
        mnu.welcome(self.firstName)
        mnu.facultyMain(self.id)
        
    
