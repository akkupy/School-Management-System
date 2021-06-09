# SCHOOL MANAGEMENT SYSTEM


import sys
import mysql.connector as msc




#     __       _       _           
#    /  \     | |     | | 
#   /    \    | | /\  | | /\   _   _
#  /  /\  \   | |/ /  | |/ /  | | | |  
# /  ____  \  | |\ \  | |\ \  | |_| |
#/__/    \__\ |_| \_\ |_| \_\  \___/
#
# Copyright of Akash, 2021          
# https://www.github.com/akkupy   
# https://t.me/akkupy   


# Def1:SPACE
def Enter():
    print()


# Def2:HORIZONTAL LINE
def Star():
    print('=' * 121)


# Def3:STUDENT MAIN MENU
def Student():
    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t STUDENTS")
        print("\t\t\t ********")
        print("\t\t 1.ADD A STUDENT")
        print("\t\t 2.DISPLAY STUDENTS")
        print("\t\t 3.EDIT THE DETAILS")
        print("\t\t 4.REMOVE A STUDENT")
        print("\t\t 5.BACK(MAIN MENU)")
        Enter()
        q = Choice("\tEnter a Choice(1,2,3,4,5 ):", [1, 2, 3, 4, 5])
        if q == 1:
            # Def6
            r = Addstudent()
            if r == 1:
                break
        elif q == 2:
            # Def7
            Displaystudent()
        elif q == 3:
            # Def8
            EditStudent()
        elif q == 4:
            # Def9
            Removestudent()
        else:
            break


# Def4:TEACHER MAIN MENU
def Teachers():
    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t TEACHERS")
        print("\t\t\t ********")
        print("\t\t 1.ADD A TEACHER")
        print("\t\t 2.DISPLAY INFORMATION OF TEACHERS")
        print("\t\t 3.EDIT THE DETAILS")
        print("\t\t 4.REMOVE A TEACHER")
        print("\t\t 5.BACK(MAIN MENU)")
        Enter()
        q = Choice("\tEnter a Choice(1,2,3,4,5 ):", [1, 2, 3, 4, 5])
        if q == 1:
            # Def10
            r = Addteachers()
            if r == 1:
                break
        elif q == 2:
            # Def11
            Displayteachers()
        elif q == 3:
            # Def12
            EditTeacher()
        elif q == 4:
            # Def13
            RemoveTeacher()
        else:
            break


# Def5:CLASS MAIN MENU
def Class():
    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t CLASS")
        print("\t\t\t *****")
        print("\t\t 1.ADD A CLASS")
        print("\t\t 2.DISPLAY ALL CLASSES")
        print("\t\t 3.EDIT THE CLASS")
        print("\t\t 4.REMOVE A CLASS")
        print("\t\t 5.BACK(MAIN MENU)")
        Enter()
        q = Choice("\tEnter a Choice(1,2,3,4,5):", [1, 2, 3, 4, 5])
        if q == 1:
            # Def14
            AddClass()
        elif q == 2:
            # Def15
            DisplayClass()
        elif q == 3:
            # Def16
            EditClass()
        elif q == 4:
            # Def17
            RemoveClass()
        else:
            break


# Def6:ADD STUDENT MENU
def Addstudent():
    Enter()
    Star()
    Enter()
    lk = []
    mycursor.execute("select class_id from Class")
    for i in mycursor:
        lk.append(i[0])
    m = Checker("\tEnter the Number of Students to Add:", "int")
    for i in range(m):
        Enter()
        Star()
        Enter()
        print("\t\tENTER THE DETAILS OF STUDENTS")
        print("\t\t*****************************")
        Enter()
        mycursor.execute("select * from Students")
        ven = mycursor.fetchall()
        h = len(ven) + 101
        print("\tDefault Admission No:", h)
        b = input("\tEnter the Student name(Max 30 Characters):")
        c = input("\tEnter the Date Of Birth(yyyy/mm/dd):")
        d = input("\tEnter the Date of Joining(yyyy/mm/dd):")
        e = input("\tEnter the gender(M/F/O):")
        f = input("\tEnter the Address(Max 50 Characters):")
        g = Checker("\tEnter the Phone Number(10 Digits):", "int")
        mycursor.execute("select class,division,class_id from Class")
        print("-" * 50)
        print("Class\t\tDivision\tClass ID")
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2])
        print("-" * 50)
        n = Checker("\tEnter the Class ID(As Per Class):", "int")
        if n not in lk:
            Enter()
            print("\t\tClass Corresponding To The Class ID Is Not Found")
            print("\t\tCreate The Class Table First!")
            print("\t\tPLEASE TRY AGAIN")
            Enter()
            Lag()
            return 1
        try:
            mycursor.execute(
                "insert into Students values({},'{}','{}','{}','{}','{}',{},{})".format(h, b, c, d, e, f, g, n))
            lib.commit()
            Enter()
            print("Student Added Successfully")
            Enter()
            Lag()
            Enter()
        except:
            Enter()
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
            yt = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if yt == 1:
                Addstudent()
            if yt == 2:
                Student()


# Def7:DISPLAY STUDENT MENU
def Displaystudent():
    def u1():
        mycursor.execute("select * from Students")
        Enter()
        print("\t\t\t ALL DETAILS OF THE STUDENT")
        print("-" * 120)
        print(
            "Admission No:\tStudent Name\tDate Of Birth\tDate Of Joining\tGender\tAddress\t    Ph Number     Class ID")
        print("-" * 120)
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2], "\t", i[3], "\t", i[4], "    ", i[5], "  ", i[6], "\t ", i[7])
            print("-" * 120)
        Enter()
        Lag()

    def u2():
        mycursor.execute("select s.student_name,c.class,c.division from students s,class c where s.class_id=c.class_id")
        Enter()
        print("\t\t\t STUDENTS WITH CLASS AND DIVISION")
        print("-" * 32)
        print("Student Name\tClass\tDivision")
        print("-" * 32)
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t", i[2])
            print("-" * 32)
        Enter()
        Lag()

    def u3():
        mycursor.execute("select s.student_name,c.class_teacher from students s,class c where s.class_id=c.class_id")
        Enter()
        print("\t\t\t STUDENTS WITH CLASS TEACHER")
        print("-" * 30)
        print("Student Name\tClass Teacher")
        print("-" * 30)
        for i in mycursor:
            print(i[0], "\t\t", i[1])
            print("-" * 30)
        Enter()
        Lag()

    def u4():
        mycursor.execute(
            "select s.student_name,c.subject1,c.subject2,c.subject3,c.subject4,c.subject5 from students s,class c where s.class_id=c.class_id")
        Enter()
        print("\t\t\t STUDENTS WITH SUBJECTS")
        print("-" * 90)
        print("Student Name\tSubject 1\tSubject 2\tSubject 3\tSubject 4\tSubject 5")
        print("-" * 90)
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4], "\t\t", i[5])
            print("-" * 90)
        Enter()
        Lag()

    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t DISPLAY STUDENTS")
        print("\t\t\t ****************")
        Enter()
        print("\t\t 1.DISPLAY ALL DETAILS OF THE STUDENT")
        print("\t\t 2.DISPLAY THE STUDENTS WITH CLASS AND DIVISION")
        print("\t\t 3.DISPLAY STUDENTS WITH CLASS TEACHER")
        print("\t\t 4.DISPLAY STUDENT WITH SUBJECTS")
        print("\t\t 5.BACK")
        Enter()
        u = Choice("\tEnter a Choice(1,2,3,4,5)", [1, 2, 3, 4, 5])
        if u == 1:
            u1()
        elif u == 2:
            u2()
        elif u == 3:
            u3()
        elif u == 4:
            u4()
        else:
            break


# Def8:EDIT STUDENT MENU
def EditStudent():
    Enter()
    mycursor.execute("select * from Students")
    print("\t\t", "-" * 13)
    print("\t\tAdmission No:")
    print("\t\t", "-" * 13)
    for i in mycursor:
        print("\t\t", i[0])
    print("\t\t", "-" * 13)
    Enter()
    p = Checker("\tEnter the Admission No:", "int")
    eh = []
    mycursor.execute("select * from Students")
    for i in mycursor:
        eh.append(i[0])
    if p in eh:
        EditStudent2(p)
    else:
        print("Enter A Valid Admission No:")
        EditStudent()


# Def8.1:EDIT STUDENT MENU 2
def EditStudent2(p):
    Enter()
    Star()
    Enter()
    print("\t\tWhat Do You Want to Edit:")
    Enter()
    print("\t 1.Student Name")
    print("\t 2.Date of Birth")
    print("\t 3.Date of Joining")
    print("\t 4.Gender")
    print("\t 5.Address")
    print("\t 6.Phone Number")
    print("\t 7.Class ID")
    print("\t 8.Exit")
    Enter()
    v = Choice("Enter Your Choice(1,2,3,4,5,6,7,8):", [1, 2, 3, 4, 5, 6, 7, 8])
    if v == 1:
        Enter()
        d = input("\tEnter the Student Name(Max 30 Characters):")
        try:
            mycursor.execute("update  Students set student_name='{}'  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tStudent Name Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 2:
        Enter()
        d = input("\tEnter the Date Of Birth(yyyy/mm/dd):")
        try:
            mycursor.execute("update  Students set date_of_birth='{}'  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tDate Of Birth Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 3:
        Enter()
        d = input("\tEnter the Date of Joining(yyyy/mm/dd):")
        try:
            mycursor.execute("update  Students set date_of_joining='{}'  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tDate Of Joining Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 4:
        Enter()
        d = input("\tEnter the Gender(M/F/O):")
        try:
            mycursor.execute("update  Students set gender='{}'  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tGender Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 5:
        Enter()
        d = input("\tEnter the Address(Max 50 Characters):")
        try:
            mycursor.execute("update  Students set address='{}'  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tAddress Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 6:
        Enter()
        d = Checker("\tEnter the Phone Number(10 Digits):", "int")
        try:
            mycursor.execute("update  Students set ph_no={}  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tPhone Number Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 7:
        Enter()
        mycursor.execute("select class,division,class_id from Class")
        print("-" * 50)
        print("Class\t\tDivision\tClass ID")
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2])
        print("-" * 50)
        Enter()
        d = input("\tEnter the Class ID(As Per Class):")
        try:
            mycursor.execute("update  Students set class_id={}  where Admission_No={}".format(d, p))
            lib.commit()
            Enter()
            print("\tClass ID Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 8:
        Student()


# Def9:REMOVE STUDENT MENU
def Removestudent():
    Enter()
    g = input("\tEnter the Admission No:")
    try:
        mycursor.execute("delete from Students where Admission_No={}".format(g))
        lib.commit()
        Enter()
        print("\tRecord With Admission No:", g, " is Deleted")
        Enter()
        Lag()
        Enter()
    except:
        print("\tEnter A Valid Admission No!")
        Enter()
        Lag()
        Enter()


# Def10:ADD TEACHERS MENU
def Addteachers():
    Enter()
    Star()
    Enter()
    lk = []
    mycursor.execute("select class_id from Class")
    for i in mycursor:
        lk.append(i[0])
    m = Checker("\tEnter the Number of Teachers to Add:", "int")
    for i in range(m):
        Enter()
        Star()
        Enter()
        print("\t\tEnter the details of the Teacher:")
        mycursor.execute("select * from Teachers")
        ven = mycursor.fetchall()
        h = len(ven) + 101
        print("\tDefault Teacher's ID:", h)
        b = input("\tEnter the Teacher name(Max 30 Characters):")
        c = input("\tEnter the Department(Max 20 Characters):")
        d = input("\tEnter the Date of Joining(yyyy/mm/dd):")
        e = input("\tEnter the gender(M/F/O):")
        f = input("\tEnter the Address(Max 50 Characters):")
        g = input("\tEnter the Phone Number(10 Digits):")
        mycursor.execute("select class,division,class_id from Class")
        print("-" * 50)
        print("Class\t\tDivision\tClass ID")
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2])
        print("-" * 50)
        w = Checker("\tEnter the Class Teacher Class ID(As Per Class):", "int")
        if w not in lk:
            Enter()
            print("\t\tClass Corresponding To The Class ID Is Not Found")
            print("\t\tCreate The Class Table First!")
            print("\t\tPLEASE TRY AGAIN")
            Enter()
            Lag()
            return 1
        try:
            mycursor.execute(
                "insert into Teachers values({},'{}','{}','{}','{}','{}','{}',{})".format(h, b, c, d, e, f, g, w))
            lib.commit()
            Enter()
            print("Teacher added successfully")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
            yt = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if yt == 1:
                Addteachers()
            if yt == 2:
                Teachers()


# Def11:DISPLAY TEACHERS MENU
def Displayteachers():
    def b1():
        mycursor.execute("select * from Teachers")
        Enter()
        print("\t\t\t ALL DETAILS OF TEACHERS")
        print("-" * 112)
        print("Teacher's ID\tTeacher's Name\tDepartment\tDate Of Joining\tGender\tAddress\t\tPh Number\tClass ID")
        print("-" * 112)
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t", i[4], "\t", i[5], "     ", i[6], "    ", i[7])
            print("-" * 112)
        Enter()
        Lag()
        Enter()

    def b2():
        mycursor.execute(
            "select t.teachers_name,c.class,c.division from teachers t,class c where t.class_id=c.class_id")
        Enter()
        print("\t\t\t TEACHER WITH CLASS TEACHER POST")
        print("-" * 32)
        print("Teacher Name\tClass\tDivision")
        print("-" * 32)
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t", i[2])
            print("-" * 32)
        Enter()
        Lag()
        Enter()

    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t DISPLAY TEACHERS")
        print("\t\t\t ****************")
        Enter()
        print("\t\t 1.DISPLAY ALL DETAILS OF THE TEACHERS")
        print("\t\t 2.DISPLAY TEACHER WITH CLASS TEACHER POST")
        print("\t\t 3.BACK")
        Enter()
        b = Choice("\tEnter a Choice(1,2,3)", [1, 2, 3])
        if b == 1:
            b1()
        elif b == 2:
            b2()
        else:
            break


# Def12:EDIT TEACHERS MENU
def EditTeacher():
    Enter()
    Enter()
    mycursor.execute("select * from Teachers")
    print("\t\t", "-" * 13)
    print("\t\tTeacher's ID:")
    print("\t\t", "-" * 13)
    for i in mycursor:
        print("\t\t", i[0])
    print("\t\t", "-" * 13)
    Enter()
    p = Checker("\tEnter the Teacher's ID:", "int")
    Enter()
    eh = []
    mycursor.execute("select * from Teachers")
    for i in mycursor:
        eh.append(i[0])
    if p in eh:
        EditTeacher2(p)
    else:
        print("Enter A Valid Teacher's ID:")
        EditTeacher()


# Def12.1:EDIT TEACHERS MENU 2
def EditTeacher2(p):
    Enter()
    Star()
    Star()
    print("\t\tWhat Do You Want to Edit")
    Enter()
    print("\t 1.Teachers Name")
    print("\t 2.Department")
    print("\t 3.Date of Joining")
    print("\t 4.Gender")
    print("\t 5.Address")
    print("\t 6.Phone Number")
    print("\t 7.Class ID")
    print("\t 8.Exit")
    Enter()
    v = Choice("Enter Your Choice(1,2,3,4,5,6,7,8):", [1, 2, 3, 4, 5, 6, 7, 8])
    if v == 1:
        Enter()
        d = input("\tEnter the Teacher's Name(Max 30 Characters):")
        try:
            mycursor.execute("update  Teachers set teachers_name='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tTeacher's Name Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 2:
        Enter()
        d = input("\tEnter the Department(Max 20 Characters):")
        try:
            mycursor.execute("update  Teachers set department='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tDepartment Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 3:
        Enter()
        d = input("\tEnter the Date of Joining(yyyy/mm/dd):")
        try:
            mycursor.execute("update  Teachers set date_of_joining='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tDate Of Joining Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 4:
        Enter()
        d = input("\tEnter the Gender(M/F/O):")
        try:
            mycursor.execute("update  Teachers set gender='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tGender Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 5:
        Enter()
        d = input("\tEnter the Address(Max 50 Characters):")
        try:
            mycursor.execute("update  Teachers set address='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tAddress Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 6:
        Enter()
        d = Checker("\tEnter the Phone Number(10 Digits):", "int")
        try:
            mycursor.execute("update  Teachers set ph_no='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tPhone Number Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 7:
        Enter()
        mycursor.execute("select class,division,class_id from Class")
        print("-" * 50)
        print("Class\t\tDivision\tClass ID")
        for i in mycursor:
            print(i[0], "\t\t", i[1], "\t\t", i[2])
        print("-" * 50)
        Enter()
        d = input("\tEnter the Class Teacher Class ID(As Per Class):")
        try:
            mycursor.execute("update  Teachers set class_id='{}'  where teachers_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tClass ID Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 8:
        Teachers()


# Def13:REMOVE TEACHERS MENU
def RemoveTeacher():
    Enter()
    g = input("Enter the Teacher's ID:")
    try:
        mycursor.execute("delete from Teachers where teachers_id={}".format(g))
        lib.commit()
        Enter()
        print("\tRecord With Teacher's ID:", g, " is Deleted")
        Enter()
        Lag()
        Enter()
    except:
        print("\tEnter A Valid Teacher's ID!")
        Enter()
        Lag()
        Enter()


# Def14:ADD CLASS MENU
def AddClass():
    Enter()
    Star()
    Enter()
    m = Checker("\tEnter the Number of Classes to Add:", "int")
    Enter()
    for i in range(m):
        Enter()
        Star()
        Enter()
        print("\t\tEnter the details of the Class")
        Enter()
        mycursor.execute("select * from Class")
        ven = mycursor.fetchall()
        h = len(ven) + 1
        print("\tDefault Class ID:", h)
        a = Checker("\tEnter the Class(Max 2 Digits):", "int")
        b = input("\tEnter the Division(Max 3 Characters):")
        c = input("\tEnter the Class Teacher(Max 20 Characters):")
        d = Checker("\tEnter the Number Of Students(Max 3 Digits):", "int")
        e = input("\tEnter Subject 1(Max 20 Characters):")
        f = input("\tEnter Subject 2(Max 20 Characters):")
        g = input("\tEnter Subject 3(Max 20 Characters):")
        k = input("\tEnter Subject 4(Max 20 Characters):")
        i = input("\tEnter Subject 5(Max 20 Characters):")
        try:
            mycursor.execute(
                "insert into Class values({},{},'{}','{}',{},'{}','{}','{}','{}','{}')".format(h, a, b, c, d, e, f, g,
                                                                                               k, i))
            lib.commit()
            Enter()
            print("Class Added Successfully")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
            yt = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if yt == 1:
                AddClass()
            if yt == 2:
                Class()


# Def15:DISPLAY CLASS MENU
def DisplayClass():
    def c1():
        mycursor.execute("select * from Class")
        Enter()
        print("\t\t\t DISPLAY ALL CLASSES")
        print("-" * 90)
        print("Class ID Class\tDivision Class Tr No Of Students  Sub 1  Sub 2  Sub 3  Sub 4     Sub 5")
        print("-" * 90)
        for i in mycursor:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4], "\t ", i[5], "\t", i[6], "\t", i[7], "  ",
                  i[8], "\t", i[9])
            print("-" * 90)
        Enter()
        Lag()
        Enter()

    def c2():
        mycursor.execute("select class,division,class_teacher from Class")
        Enter()
        print("\t\t\t CLASS WITH CLASS TEACHER")
        print("-" * 30)
        print("Class\tDivision Class Teacher")
        print("-" * 30)
        for i in mycursor:
            print(i[0], "\t", i[1], "\t", i[2])
            print("-" * 30)
        Enter()
        Lag()
        Enter()

    def c3():
        mycursor.execute("select class,division,no_of_students from Class")
        Enter()
        print("\t\t\t CLASS WITH NUMBER OF STUDENTS")
        print("-" * 32)
        print("Class\tDivision No Of Students")
        print("-" * 32)
        for i in mycursor:
            print(i[0], "\t", i[1], "\t", i[2])
            print("-" * 32)
        Enter()
        Lag()
        Enter()

    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t DISPLAY CLASSES")
        print("\t\t\t ***************")
        Enter()
        print("\t\t 1.DISPLAY ALL CLASSES")
        print("\t\t 2.DISPLAY CLASS WITH CLASS TEACHER")
        print("\t\t 3.DISPLAY CLASS WITH NUMBER OF STUDENTS")
        print("\t\t 4.BACK")
        Enter()
        c = Choice("\tEnter a Choice(1,2,3,4)", [1, 2, 3, 4])
        if c == 1:
            c1()
        elif c == 2:
            c2()
        elif c == 3:
            c3()
        else:
            break


# Def16:EDIT CLASS MENU
def EditClass():
    Enter()
    Enter()
    mycursor.execute("select * from Class")
    print("\t\t", "-" * 13)
    print("\t\tClass ID:")
    print("\t\t", "-" * 13)
    for i in mycursor:
        print("\t\t", i[0])
    print("\t\t", "-" * 13)
    Enter()
    p = int(input("Enter the Class ID:"))
    Enter()
    eh = []
    mycursor.execute("select * from Class")
    for i in mycursor:
        eh.append(i[0])
    if p in eh:
        EditClass2(p)
    else:
        print("Enter A Valid Class ID:")
        EditClass()


# Def16.1:EDIT CLASS MENU 2
def EditClass2(p):
    Enter()
    Star()
    Enter()
    print("\t\tWhat Do You Want to Edit")
    Enter()
    print("\t 1.Class")
    print("\t 2.Division")
    print("\t 3.Class Teacher")
    print("\t 4.No: of Students")
    print("\t 5.Subject 1")
    print("\t 6.Subject 2")
    print("\t 7.Subject 3")
    print("\t 8.Subject 4")
    print("\t 9.Subject 5")
    print("\t 10.Exit")
    Enter()
    v = Choice("Enter Your Choice(1,2,3,4,5,6,7,8,9,10):", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if v == 1:
        Enter()
        d = Checker("\tEnter the Class (Max 2 Digits):", "int")
        try:
            mycursor.execute("update  Class set class={}  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tClass Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()

    if v == 2:
        Enter()
        d = input("\tEnter the Division(Max 3 Characters):")
        try:
            mycursor.execute("update  Class set division='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tDivision Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 3:
        Enter()
        d = input("\tEnter the Class Teacher(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set class_teacher='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tClass Teacher Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 4:
        Enter()
        d = Checker("\tEnter the No: of Students(Max 3 Digits):", "int")
        try:
            mycursor.execute("update  Class set no_of_students={}  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tNo: of students Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 5:
        Enter()
        d = input("\tEnter the Subject 1(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject1='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 1 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 6:
        Enter()
        d = input("\tEnter the Subject 2(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject2='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 2 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 7:
        Enter()
        d = input("\tEnter the Subject 3(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject3='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 3 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 8:
        Enter()
        d = input("\tEnter the Subject 4(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject4='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 4 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 9:
        Enter()
        d = input("\tEnter the Subject 5(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject5='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 5 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 10:
        Class()


# Def17:REMOVE CLASS MENU
def RemoveClass():
    Enter()
    g = Checker("\tEnter the Class ID:", "int")
    lk = []
    mycursor.execute("select class_id from Class")
    for i in mycursor:
        lk.append(i[0])
    if g in lk:
        try:
            mycursor.execute("delete from Class where class_id={}".format(g))
            lib.commit()
            Enter()
            print("Class With Class ID", g, "is Deleted")
            Enter()
            Lag()
            Enter()
        except:
            Enter()
            print("Cannot Delete The Class As It Is Used In Other Tables")
            Enter()
            print("Delete All The Records Which Use ", g, " As Class ID From Other Tables")
            Enter()
            Lag()
            Enter()
    else:
        Enter()
        print("Enter A Valid Class ID")
        Enter()
        Lag()
        Enter()


# Def18:TABLE CREATION
def create_table():
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
def list_database():
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
def create_database():
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


# Def21:ENTER KEY FUNCTION
def Lag():
    input("Press ENTER KEY TO CONTINUE")


# Def22:INTEGER RETREIVAL CHECKING
def Checker(a, b='akku'):
    if b == "int":
        try:
            pk = int(input(a))
            return pk
        except:
            print("\tEnter As per Instruction")
            return Checker(a, b)


# Def 23:CHOICES RETRIEVAL CHECKING
def Choice(a, b):
    abc = ' '
    try:
        Enter()
        pk = int(input(a))
        if pk in b:
            abc = pk
            return abc
        else:
            Enter()
            print("\tEnter A Number As Per Instruction")
            Enter()
            Lag()
            Enter()
            return Choice(a, b)
    except:
        Enter()
        print("\tEnter A Digit As Per Instruction")
        Enter()
        Lag()
        return Choice(a, b)


# MAIN PROGRAM
Enter()
Star()
print("\t\t\t\tWELCOME TO SCHOOL MANAGEMENT SYSTEM")
Star()
Enter()
print("ENTER THE PASSWORD TO ACCESS DATABASE")
a = input(':')
Enter()
print("RE-ENTER THE PASSWORD")
b = input(':')
Enter()
y = ''
if a == b:
    y = a
else:
    Enter()
    print("PASSWORD MISMATCH!")
    sys.exit()
Enter()
v = Choice("CREATE NEW DATABASE/USE EXISTING(1,2):", [1, 2])
if v == 2:
    r = list_database()
    Enter()
    z = input("\tEnter The DataBase Name:")
    if z in r:
        Enter()
        print("\tDATABASE CHANGED")
        Enter()
        Lag()
    else:
        Enter()
        print("ENTER A VALID DATABASE OR CREATE A NEW ONE")
        sys.exit()
    Enter()

if v == 1:
    z = create_database()
    create_table()

lib = msc.connect(host="localhost", user="root", passwd=y, database=z)
mycursor = lib.cursor()
while True:
    Enter()
    Star()
    Enter()
    print("\t\t\t SCHOOL NAME WITH PLACE")
    print("\t\t\t ********************************")
    Enter()
    print("\t\t 1.STUDENTS")
    print("\t\t 2.TEACHERS")
    print("\t\t 3.CLASSES")
    print("\t\t 4.EXIT")
    Enter()
    m = Choice("\tEnter a Choice(1,2,3,4):", [1, 2, 3, 4])
    # STUDENTS
    if m == 1:
        # Def3
        Student()
    # TEACHERS
    elif m == 2:
        # Def4
        Teachers()
    # CLASS
    elif m == 3:
        # Def5
        Class()
    # EXIT
    elif m == 4:
        Enter()
        print("DATABASE CLOSED")
        Enter()
        print("PROGRAM CLOSED")
        Enter()
        Lag()
        Enter()
        break
