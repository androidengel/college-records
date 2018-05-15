"""
    Programmer:     Andrew Engel
    Date created:   2018/05/14
    Filename:       main.py
    Purpose:        main entry of course project
"""

import Menu
from Controller import createDB

def main():
    createDB()
    menu = Menu()
    id = ""
    pw = ""
    access = False
    while not access:
        id = menu.getID()
        if id == "":
            print("Username cannot be blank.")
            return
        pw = menu.getPassword()
        if pw == "":
            print("Password cannot be blank")
            return
        # place method to pass id and pw >> user class >> db