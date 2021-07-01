from .assets import *
# Def3:STUDENT MAIN MENU
def Student(mycursor,lib):
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
            r = Addstudent(mycursor,lib)
            if r == 1:
                break
        elif q == 2:
            # Def7
            Displaystudent(mycursor)
        elif q == 3:
            # Def8
            EditStudent(mycursor,lib)
        elif q == 4:
            # Def9
            Removestudent(mycursor,lib)
        else:
            break




# Def6:ADD STUDENT MENU
def Addstudent(mycursor,lib):
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
def Displaystudent(mycursor):
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
def EditStudent(mycursor,lib):
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
        EditStudent2(p,mycursor,lib)
    else:
        print("Enter A Valid Admission No:")
        EditStudent()


# Def8.1:EDIT STUDENT MENU 2
def EditStudent2(p,mycursor,lib):
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
def Removestudent(mycursor,lib):
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