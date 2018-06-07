
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       db_api.py
#Purpose:        handles db activity for application

import sqlite3

#helper function for select statements
def connectDB():
    db = sqlite3.connect('db.py')
    return db.cursor()

def createDB():
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    #create users table
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
        CREATE TABLE users (
            userid CHARACTER(20) PRIMARY KEY UNIQUE,
            firstname CHARACTER(20),
            lastname CHARACTER(20),
            email NCHAR(50),
            password CHARACTER(20),
            accesslvl CHARACTER(20)
        )
    """)
    #create faculty table
    cur.execute("DROP TABLE IF EXISTS faculty")
    cur.execute("""
        CREATE TABLE faculty (
            facultyid CHARACTER(20) PRIMARY KEY UNIQUE,
            userid CHARACTER(20),
            hiredate TEXT,
            FOREIGN KEY(userid) REFERENCES users(userid)
        )
    """)
    #create students table
    cur.execute('DROP TABLE IF EXISTS students')
    cur.execute("""
        CREATE TABLE students (
            studentid CHARACTER(20) PRIMARY KEY UNIQUE,
            userid CHARACTER(20) UNIQUE,
            enrolldate TEXT,
            gpa DOUBLE DEFAULT 0.0,
            FOREIGN KEY(userid) REFERENCES users(userid)
        )
    """)
    #create courses table
    cur.execute('DROP TABLE IF EXISTS courses')
    cur.execute("""
        CREATE TABLE courses (
            courseid CHARACTER(20) PRIMARY KEY UNIQUE,
            name NCHAR(50),
            online BOOLEAN
        )
    """)
    #create courserec table
    cur.execute('DROP TABLE IF EXISTS courserec')
    cur.execute("""
        CREATE TABLE courserec(
            recordid INTEGER PRIMARY KEY UNIQUE,
            courseid CHARACTER(20),
            professorid CHARACTER(20),
            studentlistid CHARACTER(20),
            FOREIGN KEY (courseid) REFERENCES courses(courseid),
            FOREIGN KEY (professorid) REFERENCES faculty(userid),
            FOREIGN KEY (studentlistid) REFERENCES courserecstudents(studentlistid)
        )
    """)
    #create courserecstudents table
    cur.execute('DROP TABLE IF EXISTS courserecstudents')
    cur.execute("""
        CREATE TABLE courserecstudents(
            rowid INTEGER PRIMARY KEY UNIQUE,
            studentlistid CHARACTER(20),
            studentid CHARACTER(20),
            grade DOUBLE DEFAULT 0.0,
            FOREIGN KEY (studentid) REFERENCES users(studentid)
        )
    """)
    #create studentrec table
    cur.execute('DROP TABLE IF EXISTS studentrec')
    cur.execute("""
        CREATE TABLE studentrec (
            recordid INTEGER PRIMARY KEY UNIQUE,
            studentid CHARACTER(20),
            courseid CHARACTER(20),
            FOREIGN KEY (studentid) REFERENCES students(studentid)
            FOREIGN KEY (courseid) REFERENCES courses(courseid)
        )
    """)

    #insert into users
    cur.execute("""
        INSERT INTO users (userid, firstname, lastname, email, password, accesslvl)
        VALUES ('carste', 'Carol', 'Stein', 'carol.stein@college.com', 'cmaster', 'faculty'),
        ('jimhin', 'Jim', 'Hinkins', 'jim.henkins@college.edu', 'jmaster', 'faculty'),
        ('bilmat', 'Billy', 'Matthews', 'billy.matthews@colledge.edu', 'bmaster', 'student'),
        ('kayjen', 'Kaylee', 'Jenkins', 'kaylee.jenkins@colledge.edu',  'kmaster', 'student'),
        ('marbro', 'Mary', 'Brown', 'mary.brown@colledge.edu', 'mmaster', 'student'),
        ('stejon', 'Steve', 'Jones', 'steve.jones@colledge.edu', 'smaster', 'student'),
        ('nedwil', 'Ned', 'Wilson', 'ned.wilson@colledge.edu', 'nmaster', 'student')
    """)
    #insert into students
    cur.execute("""
        INSERT INTO students (studentid, userid, enrolldate)
        VALUES ('0001', 'bilmat', '05/01/18'),
        ('0002','kayjen', '04/01/17'),
        ('0003','marbro', '01/01/18'),
        ('0004','stejon', '08/01/16'),
        ('0005','nedwil', '10/01/17')
    """)
    #insert into faculty
    cur.execute("""
        INSERT INTO faculty (facultyid, userid, hiredate)
        VALUES ('0001', 'carste', '04/01/16'),
        ('0002','jimhin','01/05/15')
    """)
    #insert into courses
    cur.execute("""
        INSERT INTO courses (courseid, name, online)
        VALUES ('0001', 'Geometry', 1),
        ('0002', 'Chemistry', 1),
        ('0003', 'Software Security', 1),
        ('0004', 'Python Programming', 0)
    """)
    #insert into courserec
    cur.execute("""
        INSERT INTO courserec (courseid, professorid, studentlistid)
        VALUES ('0002', '0001', 'A2'),
        ('0003', '0002', 'A3'),
        ('0001', '0002', 'A1'),
        ('0004', '0001', 'A4')
    """)
    #insert into courserecstudents
    cur.execute("""
        INSERT INTO courserecstudents(studentlistid, studentid, grade)
        VALUES ('A3', '0001', 95.2),
        ('A2', '0001', 82.3),
        ('A1', '0005', 100),
        ('A2', '0004', 77.1),
        ('A2', '0002', 88.6),
        ('A1', '0004', 90.7),
        ('A3', '0002', 85.4),
        ('A3', '0003', 92.4),
        ('A4', '0005', 97.7)
    """)

    db.commit()
    db.close()
    
def authenticate(id, pw):
    cur = connectDB()
    cur.execute("SELECT * FROM users WHERE userid = ? AND password = ?", (id, pw))
    return cur.fetchone()

def getStudentData(userID):
    cur = connectDB()
    cur.execute("""
        SELECT users.userid, users.firstname, users.lastname, users.email, users.password, students.enrolldate, students.gpa, users.accesslvl, students.studentid
        FROM users
        INNER JOIN students ON users.userid = students.userid
        WHERE users.userid = :id
    """, {'id':userID})
    return cur.fetchone()

def getStudentGrades(studentID):
    cur = connectDB()
    cur.execute("SELECT grade FROM courserecstudents WHERE studentid = :studentid", {'studentid':studentID})
    return cur.fetchall()

def getStudentCourses(studentID):
    cur = connectDB()
    cur.execute("""
        SELECT courses.courseid, courses.name, courses.online
        FROM studentrec
        INNER JOIN courses ON studentrec.courseid = courses.courseid
        WHERE studentrec.studentid = :studentid""", {'studentid':studentID})
    return cur.fetchall()

def getFacultyData(userID):
    cur = connectDB()
    cur.execute("""
        SELECT faculty.facultyid, users.firstname, users.lastname, users.email, users.password, faculty.hiredate
        FROM users
        INNER JOIN faculty ON users.userid = faculty.userid
        WHERE users.userid = :id""", {'id':userID})
    return cur.fetchone()
    
def getAllCourses():
    cur = connectDB()
    cur.execute('SELECT * FROM courses')
    return cur.fetchall()
        
def getCourse(id):
    cur = connectDB()
    cur.execute('SELECT * FROM courses WHERE courseid = :courseID', {'courseID':id})
    return cur.fetchone()

def numStudentsInCourse(courseID):
    cur = connectDB()
    cur.execute("SELECT studentlistid FROM courserec WHERE courseid = :courseid", {'courseid':courseID})
    listID = cur.fetchone()[0]
    cur.execute("SELECT COUNT(studentlistid) FROM courserecstudents WHERE studentlistid = :studentlistid", {'studentlistid':listID})
    return cur.fetchone()

def enroll(studentID, courseID):
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    #get studentlistid from courserec
    cur.execute("SELECT studentlistid FROM courserec WHERE courseID = :courseID", {'courseID':courseID})
    listID = cur.fetchone()
    #add student to courserecstudents
    cur.execute("""
        INSERT INTO courserecstudents (studentlistid, studentid)
        VALUES (:studentlistid, :studentid)
    """, {'studentlistid':listID[0], 'studentid':studentID})
    #add course to studentrec
    cur.execute("""
        INSERT INTO studentrec (studentid, courseid)
        VALUES (:studentid, :courseid)
    """, {'studentid':studentID, 'courseid':courseID})
    db.commit()

def isEnrolled(studentID, courseID):
    cur = connectDB()
    #get studentlistid from courserec
    cur.execute("SELECT studentlistid FROM courserec WHERE courseID = :courseID", {'courseID':courseID})
    listID = cur.fetchone()
    #confirm if already enrolled
    cur.execute("""
        SELECT studentlistid FROM courserecstudents 
        WHERE studentlistid = :studentlistid AND studentid = :studentid
        """, {'studentlistid':listID[0], 'studentid':studentID})
    dup = cur.fetchall()
    if len(dup) == 0:
        return False
    else:
        return True


def getCourseRecords(facultyID):
    cur = connectDB()
    cur.execute("""
        SELECT courserec.courseid, courses.name, users.firstname, users.lastname
        FROM courserec
        INNER JOIN courses ON courserec.courseid = courses.courseid
        INNER JOIN courserecstudents ON courserec.studentlistid = courserecstudents.studentlistid
        INNER JOIN students ON courserecstudents.studentid = students.studentid
        INNER JOIN users ON students.userid = users.userid
        WHERE courserec.professorid = :professorid
        ORDER BY courserec.courseid ASC
    """, {'professorid':facultyID})
    return cur.fetchall()


def gradeStudent(courseID, facultyID, studentID, grade):
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    #find student list ID from course records
    cur.execute("SELECT studentlistid FROM courserec WHERE courseid = :courseid AND professorid = :professorid", {'courseid':courseID, 'professorid':facultyID})
    try:
        listID = cur.fetchone()[0]
    except :
        print("Invalid Entry")
        return
    #update grade in courserecstudents table
    cur.execute("""
        UPDATE courserecstudents
        SET grade = :grade
        WHERE studentlistid = :listid AND studentid = :studentid
    """, {'grade':grade, 'listid':listID, 'studentid':studentID})
    db.commit()

def getStudentID(userID):
    cur = connectDB()
    cur.execute("SELECT studentid FROM students WHERE userid = :userid", {'userid':userID})
    try:
        id = cur.fetchone()[0]
    except :
        print("Invalid ID.")
        return
    return id
   
def updateStudentGPA(studentID, GPA):
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    cur.execute("""
        UPDATE students
        SET gpa = :gpa
        WHERE studentid = :studentid
    """, {'gpa':GPA, 'studentid':studentID})
    db.commit()