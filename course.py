
#Programmer:     Andrew Engel
#Date created:   2018/05/09
#Filename:       course.py
#Purpose:        course class file

import faculty

class Course():
    def __init__(self, id, name, online, limit = 25):
        self.id = id
        self.name = name
        self.online = online
        self.studentLimit = limit
        
