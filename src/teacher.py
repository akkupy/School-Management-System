from .assets import *
from rich import print as rprint
from rich.table import Table
from time import sleep

def Teachers(cursor,connection,console):
    while True:

        Enter()
        table = Table(title="Teachers")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Add a Teacher")
        table.add_row("2","Display Information Of Teachers")
        table.add_row("3","Edit the Details")
        table.add_row("4","Remove a Teacher")
        table.add_row("5","Go Back (Main Menu)")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3,4,5)", [1, 2, 3, 4, 5])

        match sectionValue:
            case 1:
                r = Addteachers(cursor,connection,console)
                if r == 1:
                    break
            case 2:
                Displayteachers(cursor,console)
            case 3:
                EditTeacher(cursor,connection,console)
            case 4:
                RemoveTeacher(cursor,connection,console)
            case 5:
                break


def Addteachers(cursor,connection,console):

    classes = []

    cursor.execute("select class_id from Class")
    for i in cursor:
        if i[0] == 0:
            continue
        classes.append(i[0])

    numberOfTeachers = Checker("Enter the Number of Teachers to Add:", "int")

    for i in range(numberOfTeachers):
  
        rprint("\n[bold violet]ENTER THE DETAILS OF TEACHERS\n")

        cursor.execute("select * from Teachers")
        allTeachers = cursor.fetchall()

        defaultID = len(allTeachers) + 101

        rprint("\nDefault Teacher's ID:", defaultID)
        rprint("\nEnter the Teacher name(Max 30 Characters)")
        teacherName = input(":")
        rprint("\nEnter the Department(Max 20 Characters)")
        teacherDept = input(":")
        rprint("\nEnter the Date of Joining(yyyy/mm/dd)")
        teacherDOJ = input(":")
        rprint("\nEnter the gender(M/F/O)")
        teacherGender = input(":")
        rprint("\nEnter the Address(Max 50 Characters)")
        teacherAddress = input(":")
        teacherPh = Checker("Enter the Phone Number(10 Digits):", "int")

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

        classID = Checker("Enter the Class ID(For Class Teacher, if not enter 0):", "int")
        if classID not in classes and classID!= 0:
            Enter()
            rprint("[bold red]ERROR : Class Corresponding To The Class ID Is Not Found")
            rprint("[bold green]HINT : Create The Class Table First!")
            Enter()
            Lag()
            return 1
        try:
            cursor.execute("insert into Teachers values({},'{}','{}','{}','{}','{}','{}',{})".format(defaultID, teacherName, teacherDept, teacherDOJ, teacherGender, teacherAddress, teacherPh, classID))
            connection.commit()

            Enter()
            with console.status("[bold green]Adding Details to Database...") as status:
                sleep(2)
                console.log(f'[bold][green]Teacher\'s Details Added Successfully.. ')
            Enter()
            Lag()
            Enter()

        except:
            Enter()
            rprint("[bold red]ERROR : Invalid Details Entered.")
            Enter()

            wish = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if wish == 1:
                Addteachers(cursor,connection,console)
            if wish == 2:
                return 0

def Displayteachers(cursor,console):
    def allTeachers():

        Enter()
        cursor.execute("select * from Teachers")

        table = Table(title="Display All Details Of The Teachers")
        table.add_column("Teacher's ID", style="cyan", no_wrap=True)
        table.add_column("Teacher Name", style="magenta")
        table.add_column("Department", style="magenta")
        table.add_column("Date Of Joining", style="magenta")
        table.add_column("Gender", style="magenta")
        table.add_column("Address", style="magenta")
        table.add_column("Phone Number", style="magenta")
        table.add_column("Class ID", style="magenta")
        for i in cursor:
            table.add_row(str(i[0]),i[1],i[2],str(i[3]),i[4],i[5],str(i[6]),str(i[7]))
        console.print(table)

        Enter()
        Lag()

    def teachersClass():

        Enter()
        cursor.execute("select t.teachers_id,t.teachers_name,c.class,c.division from Teachers t,Class c where t.class_id=c.class_id")

        table = Table(title="Display Teachers With Class Teacher Post")
        table.add_column("Teacher's ID", style="cyan", no_wrap=True)
        table.add_column("Teacher Name", style="magenta")
        table.add_column("Class", style="magenta")
        table.add_column("Division", style="magenta")
        for i in cursor:
            if i[2] == 0:
                continue
            table.add_row(str(i[0]),i[1],str(i[2]),i[3])
        console.print(table)

        Enter()
        Lag()


    while True:

        Enter()
        table = Table(title="Display Teachers")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Display All The Details Of The Teachers")
        table.add_row("2","Display Teacher With Class Teacher Post")
        table.add_row("3","Back")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3)", [1, 2, 3])

        if sectionValue == 1:
            allTeachers()
        elif sectionValue == 2:
            teachersClass()
        else:
            break


def EditTeacher(cursor,connection,console):

    Enter()
    cursor.execute("select * from Teachers")

    table = Table(title="Display All Teachers")
    table.add_column("Teacher's ID:", style="cyan", no_wrap=True)
    table.add_column("Teacher Name", style="magenta")
    for i in cursor:
        table.add_row(str(i[0]),i[1])
    console.print(table)
    
    teachersID = Checker("Enter the Teacher's ID:", "int")
    Enter()
    teachers = []
    cursor.execute("select * from Teachers")
    for i in cursor:
        teachers.append(i[0])
    if teachersID in teachers:
        EditTeacher2(teachersID,cursor,connection,console)
    else:
        rprint("[bold red]ERROR : Enter A Valid Teacher's ID")
        Lag()
        return 0



def EditTeacher2(teachersID,cursor,connection,console):


    Enter()
    table = Table(title="Choose What to Edit")
    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Section", style="magenta")
    table.add_row("1","Teacher Name")
    table.add_row("2","Department")
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
            rprint("\nEnter the Teacher's Name(Max 30 Characters)")
            value = input(":")
            sqlCol = 'teachers_name'
        case 2:
            rprint("\nEnter the Department(Max 20 Characters)")
            value = input(":")
            sqlCol = 'department'
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
            query = f"update  Teachers set {sqlCol}={value}  where teachers_id={teachersID}"
            cursor.execute(query)
        else:
            query = f"update  Teachers set {sqlCol}='{value}'  where teachers_id={teachersID}"
            cursor.execute(query)
        connection.commit()

        Enter()
        with console.status("[bold green]Updating Details in Database...") as status:
            sleep(2)
            console.log(f'[bold][green]Teacher Updated Successfully.. ')
        Enter()
        Lag()
        Enter()

    except:

        Enter()
        rprint("[bold red]ERROR : Invalid Value Entered.")
        Enter()
        Lag()
        return 0
    


def RemoveTeacher(cursor,connection,console):

    Enter()
    cursor.execute("select * from Teachers")

    table = Table(title="Display All Details Of The Teachers")
    table.add_column("Teacher's ID", style="cyan", no_wrap=True)
    table.add_column("Teacher Name", style="magenta")
    table.add_column("Department", style="magenta")
    table.add_column("Date Of Joining", style="magenta")
    table.add_column("Gender", style="magenta")
    table.add_column("Address", style="magenta")
    table.add_column("Phone Number", style="magenta")
    table.add_column("Class ID", style="magenta")
    for i in cursor:
        table.add_row(str(i[0]),i[1],i[2],str(i[3]),i[4],i[5],str(i[6]),str(i[7]))
    console.print(table)

    Enter()
    teachersID = Checker("Enter the Teacher's ID:", "int")
    Enter()
    teachers = []
    cursor.execute("select * from Teachers")
    for i in cursor:
        teachers.append(i[0])
    if teachersID in teachers:
        try:
            cursor.execute("delete from Teachers where teachers_id={}".format(teachersID))
            connection.commit()

            Enter()
            with console.status("[bold green]Deleting from Database...") as status:
                sleep(2)
                console.log(f'[bold][green]Record With Teacher ID: {teachersID} is Deleted Successfully.. ')
            Enter()
            Lag()
            Enter()

        except:
            Enter()
            rprint(f"[bold red]HINT : Enter A Valid Teacher's ID!")
            Enter()
            Lag()
            return 0
    else:
        Enter()
        rprint("[bold red]ERROR : Enter A Valid Class ID")
        Enter()
        Lag()
        return 0
    
