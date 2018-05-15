"""
    Programmer:     Andrew Engel
    Date created:   2018/05/14
    Filename:       menu.py
    Purpose:        menu class file
"""

class Menu():
    def __init__(self):
        errorLogin = "Access denied. Incorrect username or password."
    
    def getID(self):
        id = ""
        print("User ID: ")
        return input(id)
        
    def getPassword(self):
        pw = ""
        print("Password: ")
        return input(pw)
        
    