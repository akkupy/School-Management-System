from .assets import *
# Def4:TEACHER MAIN MENU
def Teachers(mycursor,lib):
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
            r = Addteachers(mycursor,lib)
            if r == 1:
                break
        elif q == 2:
            # Def11
            Displayteachers(mycursor)
        elif q == 3:
            # Def12
            EditTeacher(mycursor,lib)
        elif q == 4:
            # Def13
            RemoveTeacher(mycursor,lib)
        else:
            break


# Def10:ADD TEACHERS MENU
def Addteachers(mycursor,lib):
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
def Displayteachers(mycursor):
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
def EditTeacher(mycursor,lib):
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
        EditTeacher2(p,mycursor,lib)
    else:
        print("Enter A Valid Teacher's ID:")
        EditTeacher()


# Def12.1:EDIT TEACHERS MENU 2
def EditTeacher2(p,mycursor,lib):
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
def RemoveTeacher(mycursor,lib):
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
