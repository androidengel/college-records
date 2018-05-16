
#Programmer:     Andrew Engel
#Date created:   2018/05/11
#Filename:       user.py
#Purpose:        User class file

class User():
    def __init__(self, id = None, firstName = None, lastName = None, email = None, password = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
   
    @property
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
    
    def setID(self, id):
        """ send to db
            if unique
            setID
            else
            print error
        """
        
    def setPassword(self, pw):
        if len(pw) < 1:
            print("Password cannot be blank.")
        else:
            self.__password = pw
            
    def setFirstName(self, name):
        if len(name) < 1:
            print("First name cannot be blank.")
        else:
            self.__firstName = name
            
    def setLastName(self, name):
        if len(name) < 1:
            print("Last name cannot be blank.")
        else:
            self.__lastName - name
            
    def setEmail(self, email):
        if ("@" in "email" and email[-4:-3] == "."):
            self.__email = email
        else:
            print("Invalid email.")
    
    def login(self, id, pw):
        """
        lookup id and pw in database
        if record found
        login
        else print error
        """
        
