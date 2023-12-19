from .assets import *
from rich import print as rprint
from rich.table import Table
from time import sleep

# STUDENT MAIN MENU
def Student(cursor,connection,console):
    while True:

        Enter()
        table = Table(title="Students")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Add a Student")
        table.add_row("2","Display Students")
        table.add_row("3","Edit the Details")
        table.add_row("4","Remove a Student")
        table.add_row("5","Go Back (Main Menu)")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3,4,5)", [1, 2, 3, 4, 5])

        match sectionValue:
            case 1:
                r = Addstudent(cursor,connection,console)
                if r == 1:
                    break
            case 2:
                Displaystudent(cursor,console)
            case 3:
                EditStudent(cursor,connection,console)
            case 4:
                Removestudent(cursor,connection,console)
            case 5:
                break


def Addstudent(cursor,connection,console):

    classes = []

    cursor.execute("select class_id from Class")
    for i in cursor:
        if i[0] == 0:
            continue
        classes.append(i[0])

    numberOfStudents = Checker("Enter the Number of Students to Add:", "int")

    for i in range(numberOfStudents):
  
        rprint("\n[bold violet]ENTER THE DETAILS OF STUDENTS\n")

        cursor.execute("select * from Students")
        allStudents = cursor.fetchall()

        defaultAdm = len(allStudents) + 101

        rprint("\nDefault Admission No:", defaultAdm)
        rprint("\nEnter the Student name(Max 30 Characters)")
        studentName = input(":")
        rprint("\nEnter the Date Of Birth(yyyy/mm/dd)")
        studentDOB = input(":")
        rprint("\nEnter the Date of Joining(yyyy/mm/dd)")
        studentDOJ = input(":")
        rprint("\nEnter the gender(M/F/O)")
        studentGender = input(":")
        rprint("\nEnter the Address(Max 50 Characters)")
        studentAddress = input(":")
        studentPh = Checker("Enter the Phone Number(10 Digits):", "int")

        cursor.execute("select class,division,class_id from Class")

        Enter()
        table = Table(title="Class")
        table.add_column("Class", style="cyan", no_wrap=True)
        table.add_column("Division", style="magenta")
        table.add_column("Class ID", style="violet")
        for i in cursor:
            if i[2] == 0:
                continue
            table.add_row(str(i[0]),i[1],str(i[2]))

        console.print(table)

        classID = Checker("Enter the Class ID(As Per Class):", "int")
        if classID not in classes:
            Enter()
            rprint("[bold red]ERROR : Class Corresponding To The Class ID Is Not Found")
            rprint("[bold green]HINT : Create The Class Table First!")
            Enter()
            Lag()
            return 1
        try:

            cursor.execute(
                "insert into Students values({},'{}','{}','{}','{}','{}',{},{})".format(defaultAdm, studentName, studentDOB, studentDOJ, studentGender, studentAddress, studentPh, classID))
            connection.commit()

            Enter()
            with console.status("[bold green]Adding Details to Database...") as status:
                sleep(2)
                console.log(f'[bold][green]Student Details Added Successfully.. ')
            Enter()
            Lag()
            Enter()

        except:
            Enter()
            rprint("[bold red]ERROR : Invalid Details Entered.")
            Enter()

            wish = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if wish == 1:
                Addstudent(cursor,connection,console)
            if wish == 2:
                return 0


# Def7:DISPLAY STUDENT MENU
def Displaystudent(cursor,console):
    def allStudents():

        Enter()
        cursor.execute("select * from Students")

        table = Table(title="Display All Details Of The Student")
        table.add_column("Admission No", style="cyan", no_wrap=True)
        table.add_column("Student Name", style="magenta")
        table.add_column("Date Of Birth", style="magenta")
        table.add_column("Date Of Joining", style="magenta")
        table.add_column("Gender", style="magenta")
        table.add_column("Address", style="magenta")
        table.add_column("Phone Number", style="magenta")
        table.add_column("Class ID", style="magenta")
        for i in cursor:
            table.add_row(str(i[0]),i[1],str(i[2]),str(i[3]),i[4],i[5],str(i[6]),str(i[7]))
        console.print(table)

        Enter()
        Lag()

    def studentClass():

        Enter()
        cursor.execute("select s.student_name,c.class,c.division from Students s,Class c where s.class_id=c.class_id")

        table = Table(title="Display Student With Class And Division")
        table.add_column("Student Name", style="cyan", no_wrap=True)
        table.add_column("Class", style="magenta")
        table.add_column("Division", style="magenta")
        for i in cursor:
            table.add_row(i[0],str(i[1]),i[2])
        console.print(table)

        Enter()
        Lag()

    def studentClassTeacher():

        Enter()
        cursor.execute("select s.student_name,c.class_teacher from Students s,Class c where s.class_id=c.class_id")

        table = Table(title="Display Student With Class Teacher")
        table.add_column("Student Name", style="cyan", no_wrap=True)
        table.add_column("Class Teacher", style="magenta")
        for i in cursor:
            table.add_row(i[0],i[1])
        console.print(table)

        Enter()
        Lag()

    def studentSubject():

        Enter()
        cursor.execute("select s.student_name,c.subject1,c.subject2,c.subject3,c.subject4,c.subject5 from Students s,Class c where s.class_id=c.class_id")

        table = Table(title="Display Student With Subjects")
        table.add_column("Student Name", style="cyan", no_wrap=True)
        table.add_column("Subject 1", style="magenta")
        table.add_column("Subject 2", style="magenta")
        table.add_column("Subject 3", style="magenta")
        table.add_column("Subject 4", style="magenta")
        table.add_column("Subject 5", style="magenta")
        for i in cursor:
            table.add_row(i[0],i[1],i[2],i[3],i[4],i[5])
        console.print(table)

        Enter()
        Lag()

    while True:

        Enter()
        table = Table(title="Display Students")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Display All The Details Of The Student")
        table.add_row("2","Display The Students With Class and Division")
        table.add_row("3","Display Student With Class Teacher")
        table.add_row("4","Display Student With Subjects")
        table.add_row("5","Back")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3,4,5)", [1, 2, 3, 4,5])

        if sectionValue == 1:
            allStudents()
        elif sectionValue == 2:
            studentClass()
        elif sectionValue == 3:
            studentClassTeacher()
        elif sectionValue == 4:
            studentSubject()
        else:
            break



def EditStudent(cursor,connection,console):

    Enter()
    cursor.execute("select * from Students")

    table = Table(title="Display All Students")
    table.add_column("Admission No:", style="cyan", no_wrap=True)
    table.add_column("Student Name", style="magenta")
    for i in cursor:
        table.add_row(str(i[0]),i[1])
    console.print(table)
    
    studentAdm = Checker("Enter the Admission No:", "int")
    Enter()
    students = []
    cursor.execute("select * from Students")
    for i in cursor:
        students.append(i[0])
    if studentAdm in students:
        EditStudent2(studentAdm,cursor,connection,console)
    else:
        rprint("[bold red]ERROR : Enter A Valid Admission No:")
        Lag()
        return 0


def EditStudent2(studentAdm,cursor,connection,console):

    Enter()
    table = Table(title="Choose What to Edit")
    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Section", style="magenta")
    table.add_row("1","Student Name")
    table.add_row("2","Date Of Birth")
    table.add_row("3","Date Of Joining")
    table.add_row("4","Gender")
    table.add_row("5","Address")
    table.add_row("6","Phone Number")
    table.add_row("7","Class ID")
    table.add_row("8","Exit")
    console.print(table)
    sectionValue = Choice("Enter Your Choice(1,2,3,4,5,6,7,8)", [1, 2, 3, 4, 5, 6, 7, 8])

    match sectionValue:
        case 1:
            rprint("\nEnter the Student Name(Max 30 Characters)")
            value = input(":")
            sqlCol = 'student_name'
        case 2:
            rprint("\nEnter the Date Of Birth(yyyy/mm/dd)")
            value = input(":")
            sqlCol = 'date_of_birth'
        case 3:
            rprint("\nEnter the Date of Joining(yyyy/mm/dd)")
            value = input(":")
            sqlCol = 'date_of_joining'
        case 4:
            rprint("\nEnter the Gender(M/F/O)")
            value = input(":")
            sqlCol = 'gender'
        case 5:
            rprint("\nEnter the Address(Max 50 Characters)")
            value = input(":")
            sqlCol = 'address'
        case 6:
            value = Checker("Enter the Phone Number(10 Digits)", "int")
            sqlCol = 'ph_no'
        case 7:
            Enter()
            cursor.execute("select * from Class")

            table = Table(title="Display All Classes")
            table.add_column("Class ID", style="cyan", no_wrap=True)
            table.add_column("Class", style="magenta")
            table.add_column("Division", style="magenta")
            for i in cursor:
                if i[0] == 0:
                    continue
                table.add_row(str(i[0]),str(i[1]),i[2])
            console.print(table)
            
            value = Checker("Enter the Class ID:", "int")
            Enter()
            classes = []
            cursor.execute("select * from Class")
            for i in cursor:
                if i[0] == 0:
                    continue
                classes.append(i[0])
            sqlCol = 'class_id'
            if value not in classes:
                rprint("[bold red]ERROR : Enter A Valid Class ID")
                Lag()
                return 0
            
        case 8:
            return 0
        
    try:
        if type(value) is int:
            query = f"update  Students set {sqlCol}={value}  where Admission_No={studentAdm}"
            cursor.execute(query)
        else:
            query = f"update  Students set {sqlCol}='{value}'  where Admission_No={studentAdm}"
            cursor.execute(query)
        connection.commit()

        Enter()
        with console.status("[bold green]Updating Details in Database...") as status:
            sleep(2)
            console.log(f'[bold][green]Student Updated Successfully.. ')
        Enter()
        Lag()
        Enter()

    except:

        Enter()
        rprint("[bold red]ERROR : Invalid Value Entered.")
        Enter()
        Lag()
        return 0
    
def Removestudent(cursor,connection,console):

    Enter()
    cursor.execute("select * from Students")

    table = Table(title="Display All Details Of The Student")
    table.add_column("Admission No", style="cyan", no_wrap=True)
    table.add_column("Student Name", style="magenta")
    table.add_column("Date Of Birth", style="magenta")
    table.add_column("Date Of Joining", style="magenta")
    table.add_column("Gender", style="magenta")
    table.add_column("Address", style="magenta")
    table.add_column("Phone Number", style="magenta")
    table.add_column("Class ID", style="magenta")
    for i in cursor:
        table.add_row(str(i[0]),i[1],str(i[2]),str(i[3]),i[4],i[5],str(i[6]),str(i[7]))
    console.print(table)

    Enter()
    studentAdm = Checker("Enter the Admission No:", "int")
    Enter()
    students = []
    cursor.execute("select * from Students")
    for i in cursor:
        students.append(i[0])
    if studentAdm in students:
        try:
            cursor.execute("delete from Students where Admission_No={}".format(studentAdm))
            connection.commit()

            Enter()
            with console.status("[bold green]Deleting from Database...") as status:
                sleep(2)
                console.log(f'[bold][green]Record With Admission No: {studentAdm} is Deleted Successfully.. ')
            Enter()
            Lag()
            Enter()

        except:
            Enter()
            rprint(f"[bold red]HINT : Enter A Valid Admission No!")
            Enter()
            Lag()
            return 0
    else:
        Enter()
        rprint("[bold red]ERROR : Enter A Valid Class ID")
        Enter()
        Lag()
        return 0
    