import sqlite3 as lite

#def main( ):
#   AddNewCourse()

# e ray is handsome

def All(): #show all course
    con = lite.connect('CourseSystem.db')
    cur = con.cursor()
    print("All Course:")
    command = "SELECT class_id FROM course "
    cur.execute(command)
    rows = cur.fetchall()
    ###
    for row in rows:
        print("Class ID:" + row[0])

def Details(): #show select course detail
    con = lite.connect('CourseSystem.db')
    cur = con.cursor()
    class_id = input("Enter Class ID:")
    # find class id in data base
    command = "SELECT * FROM course WHERE class_id = '" + class_id + "'"
    cur.execute(command)
    row = cur.fetchone()
    ###
    if row==None: #no data
        print("Class ID Not Found")
        return False
    else:
        print("########################")
        print("# Class ID       :",row[1])  #class_id
        print("# Professor      :",row[2])  #professor
        print("# Title          :",row[3])  #title
        print("# Student Number :",row[4])  #student_number
        print("# Week           :",row[5])  #cweek
        print("# Time           :",row[6])  #ctime
        print("########################")

def AddNewCourse():
    con = lite.connect('CourseSystem.db')
    cur = con.cursor()
    ###
    print("Enter class information to Update")
    class_id =       input("class id       : ")
    professor =      input("professor      : ")
    title =          input("title          : ")
    student_number = input("student_number : ")
    cweek =          input("week           : ")
    ctime =          input("time           : ")
    ###
    with con:
        cur = con.cursor()
        command = f"Insert into course Values(null, '{class_id}','{professor}', '{title}', '{student_number}', '{cweek}', '{ctime}')"
        cur.execute(command)
    print("Successfully Update")

