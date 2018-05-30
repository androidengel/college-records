
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
    print('create users table')
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
    print('create faculty table')
    cur.execute("DROP TABLE IF EXISTS faculty")
    cur.execute("""
        CREATE TABLE faculty (
            facultyid SMALLINT PRIMARY KEY UNIQUE,
            userid CHARACTER(20),
            hiredate TEXT,
            FOREIGN KEY(userid) REFERENCES users(userid)
        )
    """)
    #create students table
    print('create students table')
    cur.execute('DROP TABLE IF EXISTS students')
    cur.execute("""
        CREATE TABLE students (
            studentid SMALLINT PRIMARY KEY UNIQUE,
            userid CHARACTER(20) UNIQUE,
            enrolldate TEXT,
            gpa DOUBLE,
            FOREIGN KEY(userid) REFERENCES users(userid)
        )
    """)
    #create courses table
    print('create courses table')
    cur.execute('DROP TABLE IF EXISTS courses')
    cur.execute("""
        CREATE TABLE courses (
            courseid CHARACTER(20) PRIMARY KEY UNIQUE,
            name NCHAR(50),
            online BOOLEAN
        )
    """)
    #create courserec table
    print('create courserec table')
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
    print('create courserecstudents table')
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
    print('create studentrec table')
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

    print('insert rows')
    #insert into users
    cur.execute("""
        INSERT INTO users (userid, firstname, lastname, email, password, accesslvl)
        VALUES ('0001', 'admin', 'admin', 'admin@admin.com', 'password', 'root'),
        ('0002', 'Jim', 'Hinkins', 'jim.henkins@college.edu', 'jmaster', 'faculty'),
        ('0003', 'Billy', 'Matthews', 'billy.matthews@colledge.edu', 'bmaster', 'student'),
        ('0004', 'Kaylee', 'Jenkins', 'kaylee.jenkins@colledge.edu',  'kmaster', 'student'),
        ('0005', 'Mary', 'Brown', 'mary.brown@colledge.edu', 'mmaster', 'student'),
        ('0006', 'Steve', 'Jones', 'steve.jones@colledge.edu', 'smaster', 'student'),
        ('0007', 'Ned', 'Wilson', 'ned.wilson@colledge.edu', 'nmaster', 'student')
    """)
    #insert into students
    cur.execute("""
        INSERT INTO students (studentid, userid, enrolldate, gpa)
        VALUES ('0001', '0003', '05/01/18', 3.8),
        ('0002','0004', '04/01/17', 3.7),
        ('0003','0005', '01/01/18', 3.2),
        ('0004','0006', '08/01/16', 3.9),
        ('0005','0007', '10/01/17', 2.4)
    """)
    #insert into faculty
    cur.execute("""
        INSERT INTO faculty (facultyid, userid, hiredate)
        VALUES ('0001', '0002', '04/01/16')
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
        INSERT INTO courserecstudents(studentlistid, studentid)
        VALUES ('A3', '0001'),
        ('A2', '0001'),
        ('A1', '0005'),
        ('A2', '0004'),
        ('A2', '0002'),
        ('A1', '0004'),
        ('A3', '0002'),
        ('A3', '0003'),
        ('A4', '0005')
    """)

    print('commit')
    db.commit()
    print('display')
    for row in cur.execute('SELECT * FROM users'):
        print(row)
    print('close')
    db.close()
    
def authenticate(id, pw):
    cur = connectDB()
    cur.execute("SELECT * FROM users WHERE userid = ? AND password = ?", (id, pw))
    return cur.fetchone()

def getStudentData(studentID):
    cur = connectDB()
    cur.execute("""
        SELECT users.userid, users.firstname, users.lastname, users.email, users.password, students.enrolldate, students.gpa, users.accesslvl
        FROM users
        INNER JOIN students ON users.userid = students.userid
        WHERE users.userid = :id""", {'id':studentID})
    return cur.fetchone()

def getStudentCourses(studentID):
    cur = connectDB()
    cur.execute("""
        SELECT courses.courseid, courses.name, courses.online
        FROM studentrec
        INNER JOIN courses ON studentrec.courseid = courses.courseid
        WHERE studentrec.studentid = :studentid""", {'studentid':studentID})
    return cur.fetchall()

def getFacultyData(facultyID):
    cur = connectDB()
    cur.execute("""
        SELECT users.userid, users.firstname, users.lastname, users.email, users.password, faculty.hiredate
        FROM users
        INNER JOIN faculty ON users.userid = faculty.userid
        WHERE users.userid = :id""", {'id':facultyID})
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
    cur = connectDB()
    #find student list ID from course records
    cur.execute("SELECT studentlistid FROM courserec WHERE courseid = :courseid AND professorid = :professorid", {'courseid':courseID, 'professorid':facultyID})
    listID = cur.fetchone()[0]
    #update grade in courserecstudents table
    cur.execute("""
        UPDATE courserecstudents
        SET grade = :grade
        WHERE studentlistid = :listid AND studentid = :studentid
    """, {'grade':grade, 'listid':listID, 'studentid':studentID})
    #TESTING PURPOSES BELOW
    cur.execute("SELECT * FROM courserecstudents WHERE studentlistid = :studentlistid AND studentid = :studentid", {'studentlistid':listID, 'studentid':studentID})
    return cur.fetchone()

#***************TESTING FUNCTIONS*****************

def getAllStudentRecords():
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    cur.execute("SELECT * FROM studentrec")
    return cur.fetchall()

def getAllCourseRecords():
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    cur.execute("SELECT * FROM courserec")
    return cur.fetchall()