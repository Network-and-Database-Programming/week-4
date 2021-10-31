import sqlite3 as lite
import os
def Login():         ## return true if login success, false if login fail
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "CourseSystem.db")
    con = lite.connect(db_path)
    print("Enter your Login information:")
    account = input("account:")     ## Input account
    cur=con.cursor()
    command = "select * from student WHERE account = '" + account + "'"
    cur.execute(command) 
    row=cur.fetchone()
    ###
    if row==None:                   ## Not register yet
        print("Account Not Found")
        return False
    ###
    Password = input("password:")   ## Input Password

    if row[6] == Password :         ## successfully login
        print("you are successfully login now")
        return True
    else :                          ## Password Error
        print("Password Incorrect")
        return False

def Register():             ## Sign Up account
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "CourseSystem.db")
    con = lite.connect(db_path)
    cur=con.cursor()
    ###
    print("Enter account information to Sign up")
    student_id =   input("studentID:")
    name =   input("name:")
    grade =   input("grade:")
    major =   input("major:")
    ## check if account is already used
    while True:
        account =   input("account:")
        command = "select * from student WHERE account = '" + account + "'"
        cur.execute(command)
        row=cur.fetchone()
        if row != None:
            print("account is already used, enter another one")
        else:
            break
    ##
    password =   input("password:")
    with con:
        cur=con.cursor()
        command = f"Insert into student Values(null, '{student_id}', '{name}', {grade}, '{major}', '{account}', '{password}')"
        cur.execute(command)
    print("Successfully sign up")
# Login()
# Register()
