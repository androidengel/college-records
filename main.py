
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       main.py
#Purpose:        main entry of course project

import os
import menu
import controller
import student
import faculty

def main():
    print('Building database ...')
    controller.createDB()
    menu1 = menu.Menu()
    id = ""
    pw = ""
    userRecord = None

    authorized = False
    while not authorized:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("School Records Application")
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
            input("Press enter to continue ...")
    #end while

    id = userRecord[0]
    privilege = userRecord[5]
    choice = ""
    if privilege == 'student':
        data = controller.getStudentData(id)
        st = student.Student(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        os.system('cls' if os.name == 'nt' else 'clear')
        menu1.welcome(st.firstName)
        while choice != "0":
            choice = menu1.studentMain(st.id)
            if choice == '1':
                menu1.viewStudentRecord(st.id)
            elif choice == '2':
                menu1.viewAllCourses()
            elif choice == '3':
                course1 = menu1.enrollMenu() #returns Course object
                numStudents = controller.numStudentsInCourse(course1.id)
                if numStudents[0] >= course1.studentLimit:
                    print("This class is full. Enrollment Aborted.")
                    return
                #check if already enrolled
                enrolled = controller.isEnrolled(st.id, course1.id)
                if enrolled:
                    print(f"You are already enrolled in {course1.name}.")
                else:
                    controller.enroll(st.id, course1.id)
                    print("You are now enrolled.")
            elif choice == '0':
                print("Goodbye!")
                return
            else:
                print("Invalid entry.\n")
            #pause and clear console
            input("Press Enter to continue ...")
            os.system('cls' if os.name == 'nt' else 'clear')
        #End while
    elif privilege == 'faculty':
        data = controller.getFacultyData(id)
        fac = faculty.Faculty(data[0], data[1], data[2], data[3], data[4], data[5])
        os.system('cls' if os.name == 'nt' else 'clear')
        menu1.welcome(fac.firstName)
        while choice != '0':
            choice = menu1.facultyMain(fac.id)
            if choice == '1':
                menu1.facViewStudentRecord()
            elif choice == '2':
                menu1.viewCourseRecords(fac.id)
            elif choice == '3':
                menu1.gradeStudent(fac.id)
            elif choice == '0':
                print("Goodbye!")
            else:
                print("Invalid entry.\n")
            #pause and clear console
            input("Press Enter to continue ...")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()