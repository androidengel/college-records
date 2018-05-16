
#Programmer:     Andrew Engel
#Date created:   2018/05/14
#Filename:       db_api.py
#Purpose:        handles db activity for application

import sqlite3

def createDB():
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    #create users table
    print('create users table')
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
        CREATE TABLE users (
            userid CHARACTER(20) PRIMARY KEY,
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
            facultyid SMALLINT PRIMARY KEY,
            userid CHARACTER(20),
            hiredate DATETIME,
            FOREIGN KEY(userid) REFERENCES users(userid)
        )
    """)
    #create students table
    print('create students table')
    cur.execute('DROP TABLE IF EXISTS students')
    cur.execute("""
        CREATE TABLE students (
            studentid SMALLINT PRIMARY KEY,
            userid CHARACTER(20),
            enrolldate DATETIME,
            gpa DOUBLE,
            FOREIGN KEY(userid) REFERENCES users(userid)
        )
    """)
    #create courses table
    print('create courses table')
    cur.execute('DROP TABLE IF EXISTS courses')
    cur.execute("""
        CREATE TABLE courses (
            courseid CHARACTER(20) PRIMARY KEY,
            name NCHAR(50),
            online BOOLEAN
        )
    """)
    #create courserec table
    print('create courserec table')
    cur.execute('DROP TABLE IF EXISTS courserec')
    cur.execute("""
        CREATE TABLE courserec(
            recordid SMALLINT PRIMARY KEY,
            courseid CHARACTER(20),
            professorid CHARACTER(20),
            studentid CHARACTER(20),
            FOREIGN KEY (courseid) REFERENCES courses(courseid),
            FOREIGN KEY (professorid) REFERENCES faculty(userid),
            FOREIGN KEY (studentid) REFERENCES students(userid)
        )
    """)
    #create studentrec table
    print('create studentrec table')
    cur.execute('DROP TABLE IF EXISTS studentrec')
    cur.execute("""
        CREATE TABLE studentrec (
            recordid SMALLINT PRIMARY KEY,
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
        ('0003', 'Billy', 'Matthews', 'billy.matthews@colledge.edu', 'bmaster', 'student')
    """)
    #insert into students
    cur.execute("""
        INSERT INTO students (studentid, userid, enrolldate, gpa)
        VALUES ('0001', '0003', 05/01/18, 0.0)
    """)
    #insert into faculty
    cur.execute("""
        INSERT INTO faculty (facultyid, userid, hiredate)
        VALUES ('0001', '0002', 04/01/16)
    """)
    #insert into courses
    cur.execute("""
        INSERT INTO courses (courseid, name, online)
        VALUES ('0001', 'Geometry', 1),
        ('0002', 'Chemistry', 1),
        ('0003', 'Software Security', 1),
        ('0004', 'Python Programming', 0)
    """)

    print('commit')
    db.commit()
    print('display')
    for row in cur.execute('SELECT * FROM users'):
        print(row)
    print('close')
    db.close()
    
def authenticate(id, pw):
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE userid = ? AND password = ?", (id, pw))
    return cur.fetchone()

def getStudentData(studentID):
    db = sqlite3.connect('db.py')
    cur = db.cursor()
    cur.execute("""
        SELECT users.userid, users.firstname, users.lastname, users.email, users.password, students.enrolldate, students.gpa
        FROM users
        INNER JOIN students ON users.userid = students.userid
        WHERE users.userid = :id""", {'id':studentID})
    return cur.fetchone()
    
def getAllCourses():
    cur.execute('SELECT * FROM courses')
    return cur.fetchall()
        
def getCourse(id):
    cur.execute("SELECT * FROM courses WHERE courseid = :courseID", {'courseID':id})
    return cur.fetchone()
