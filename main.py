
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       main.py
#Purpose:        main entry of course project

import menu
import controller
import student
import faculty

def main():
    controller.createDB()
    menu1 = menu.Menu()
    id = ""
    pw = ""
    userRecord = None

    authorized = False
    while not authorized:
        #get id and password from user
        id = menu1.getID()
        if id == "":
            print("Username cannot be blank.")
            return
        pw = menu1.getPassword()
        if pw == "":
            print("Password cannot be blank")
            return
        #authenticate
        userRecord = controller.authenticate(id, pw)
        if userRecord != None:
            authorized = True
        else:
            print("Invalid login - Access denied")
    #end while

    id = userRecord[0]
    privilege = userRecord[5]
    if privilege == 'student':
        data = controller.getStudentData(id)
        st = student.Student(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        menu1.welcome(st.firstName)
        st.login(menu1)


if __name__ == '__main__':
    main()