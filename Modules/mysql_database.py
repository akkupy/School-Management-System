import sys,mysql.connector as msc
from .assets import *
# Def18:TABLE CREATION
def create_table(y,z):
    mydb = msc.connect(host="localhost", user="root", passwd=y, database=z)
    mycursor = mydb.cursor()
    Enter()
    print("\tCreating Class table......Please Wait..")
    sql = "CREATE TABLE if not exists Class(class_id int(5) PRIMARY KEY,class int(2),division varchar(3),class_teacher varchar(20),no_of_students int(3),subject1 varchar(20),subject2 varchar(20),subject3 varchar(20),subject4 varchar(20),subject5 varchar(20));"
    mycursor.execute(sql)
    print("\t\tClass table created")
    Enter()
    Lag()
    Enter()
    print("\tCreating Students table......Please Wait..")
    sql = "CREATE TABLE if not exists Students(Admission_No int(10) PRIMARY KEY,student_name varchar(30) NOT NULL, date_of_birth date,date_of_joining date, gender varchar(2),address varchar(50),ph_no varchar(11),class_id int(5));"
    mycursor.execute(sql)
    sql1 = "ALTER TABLE Students Add FOREIGN KEY(class_id) references Class(class_id);"
    mycursor.execute(sql1)
    Enter()
    print("\t\tStudents Table Created")
    Enter()
    Lag()
    Enter()
    print("\tCreating Teachers table......Please Wait..")
    sql = "CREATE TABLE if not exists Teachers(teachers_id int(5)PRIMARY KEY,teachers_name varchar(30) NOT NULL,department varchar(20),date_of_joining date,gender varchar(2),address varchar(50), ph_no varchar(11),class_id int(5));"
    mycursor.execute(sql)
    sql1 = "ALTER TABLE Teachers Add FOREIGN KEY(class_id) references Class(class_id);"
    mycursor.execute(sql1)
    print("\t\tTeachers table created")
    Enter()
    Enter()
    print("\tDATABASE AND TABLES ARE CREATED")
    Enter()
    Lag()
    Enter()


# Def19:LISTING THE DATABASES
def list_database(y):
    try:
        mydb = msc.connect(host="localhost", user="root",
                           password=y)
        mycursor = mydb.cursor()
        sql = "show databases;"
        mycursor.execute(sql)
        Enter()
        print("-" * 20)
        print("DATABASE NAME")
        print("-" * 20)
        list = []
        for i in mycursor:
            print(i[0])
            list.append(i[0])
        print("-" * 20)
        return list
    except:
        Enter()
        print("ACCESS DENIED")
        Enter()
        print("INCORRECT PASSWORD")
        sys.exit()


# Def20:CREATING A NEW DATABASE
def create_database(y):
    try:
        mydb = msc.connect(host="localhost", user="root",
                           password=y)
        mycursor = mydb.cursor()
        Enter()
        z = input("Enter New Database:")
        sql = "create database " + z
        mycursor.execute(sql)
        Enter()
        print("DATABASE CREATED")
        Lag()
        return z
    except:
        Enter()
        print('ACCESS DENIED')
        Enter()
        print('INCORRECT PASSWORD')
        sys.exit()