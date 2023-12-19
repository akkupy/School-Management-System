from .assets import *
from time import sleep
# TABLE CREATION
def create_table(cursor,console):

    with console.status("[bold green]Checking/Creating Class Table..") as status:
        sleep(2)
        query = "CREATE TABLE if not exists Class(class_id int(5) PRIMARY KEY,class int(2),division varchar(10),class_teacher varchar(50),no_of_students int(3),subject1 varchar(20),subject2 varchar(20),subject3 varchar(20),subject4 varchar(20),subject5 varchar(20));"
        cursor.execute(query)
        cursor.execute("select * from Class")
        flag = False
        for i in cursor:
            if i[0] == 0:
                flag = True
        if not flag:
            query = "insert into Class values({},{},'{}','{}',{},'{}','{}','{}','{}','{}')".format(0, 0, 'Class 0', 'For Non Class Teacher', 0, 'Nil', 'Nil', 'Nil', 'Nil', 'Nil')
            cursor.execute(query)
        console.log(f"[green]Done.[/green]")

    with console.status("[bold green]Checking/Creating Students Table..") as status:
        sleep(2)
        query = "CREATE TABLE if not exists Students(Admission_No int(10) PRIMARY KEY,student_name varchar(30) NOT NULL, date_of_birth date,date_of_joining date, gender varchar(2),address varchar(50),ph_no varchar(11),class_id int(5));"
        cursor.execute(query)
        query = "ALTER TABLE Students Add FOREIGN KEY(class_id) references Class(class_id);"
        cursor.execute(query)
        console.log(f"[green]Done.[/green]")
 
    with console.status("[bold green]Checking/Creating Teachers Table..") as status:
        sleep(2)
        query = "CREATE TABLE if not exists Teachers(teachers_id int(5)PRIMARY KEY,teachers_name varchar(30) NOT NULL,department varchar(20),date_of_joining date,gender varchar(2),address varchar(50), ph_no varchar(11),class_id int(5) DEFAULT 0);"
        cursor.execute(query)
        query = "ALTER TABLE Teachers Add FOREIGN KEY(class_id) references Class(class_id);"
        cursor.execute(query)
        console.log(f"[green]Done.[/green]")
    

# CREATE NEW DATABASE
def create_database(cursor,console):
    with console.status("[bold green]Creating New Database..") as status:
        sleep(3)
        query = "CREATE DATABASE IF NOT EXISTS school;"
        cursor.execute(query)
        console.log("[green]Database Created![/green]")
    return 'school'
