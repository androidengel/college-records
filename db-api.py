#   Programmer:     Andrew Engel
#   Date created:   2018/05/14
#   Filename:       db-api.py
#   Purpose:        handles db activity for application

import sqlite3

def createDB():
    db = sqlite3.connect('db-api.db')
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
            password CHARACTER(20)
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
        INSERT INTO users (userid, firstname, lastname, email, password)
        VALUES ('0001', 'admin', 'admin', 'admin@admin.com', 'password'),
        ('0002', 'Jim', 'Hinkins', 'jim.henkins@college.edu', 'jmaster'),
        ('0003', 'Billy', 'Matthews', 'billy.matthews@colledge.edu', 'bmaster')
    """)

    print('commit')
    db.commit()
    print('display')
    for row in cur.execute('SELECT * FROM users'):
        print(row)
    print('close')
    db.close()