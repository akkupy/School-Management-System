from .assets import *
from rich import print as rprint
from rich.table import Table
from time import sleep

# Def5:CLASS MAIN MENU
def Class(cursor,connection,console):
    while True:

        Enter()
        table = Table(title="Class")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Add a Class")
        table.add_row("2","Display all classes")
        table.add_row("3","Edit the Class")
        table.add_row("4","Remove a Class")
        table.add_row("5","Go Back (Main Menu)")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3,4,5)", [1, 2, 3, 4, 5])

        if sectionValue == 1:
            AddClass(cursor,connection,console)
        elif sectionValue == 2:
            DisplayClass(cursor,console)
        elif sectionValue == 3:
            EditClass(cursor,connection,console)
        elif sectionValue == 4:
            RemoveClass(cursor,connection)
        else:
            break

def AddClass(cursor,connection,console):

    numberOfClasses = Checker("Enter the Number of Classes to Add:", "int")

    for i in range(numberOfClasses):

        rprint("\n[bold violet]ENTER THE DETAILS OF THE CLASS\n")

        cursor.execute("select * from Class")
        allClasses = cursor.fetchall()
        defaultCLassID = len(allClasses) + 1


        rprint("\nDefault Class ID:", defaultCLassID)

        classNum = Checker("Enter the Class(Max 2 Digits):", "int")

        rprint("\nEnter the Division(Max 3 Characters)")
        classDiv = input(":")
        rprint("\nEnter the Class Teacher(Max 20 Characters)")
        classTeacher = input(":")
        classNumStudents = Checker("Enter the Number Of Students(Max 3 Digits):", "int")
        rprint("\nEnter Subject 1(Max 20 Characters)")
        classSubject1 = input(":")
        rprint("\nEnter Subject 2(Max 20 Characters)")
        classSubject2 = input(":")
        rprint("\nEnter Subject 3(Max 20 Characters)")
        classSubject3 = input(":")
        rprint("\nEnter Subject 4(Max 20 Characters)")
        classSubject4 = input(":")
        rprint("\nEnter Subject 5(Max 20 Characters)")
        classSubject5 = input(":")
        
        try:
            cursor.execute(
                "insert into Class values({},{},'{}','{}',{},'{}','{}','{}','{}','{}')".format(defaultCLassID, classNum, classDiv, classTeacher, classNumStudents, classSubject1, classSubject2, classSubject3, classSubject4, classSubject5))
            connection.commit()

            Enter()
            with console.status("[bold green]Adding Details to Database...") as status:
                sleep(2)
                console.log(f'[bold][green]Class Created Successfully.. ')
            Enter()
            Lag()
            Enter()

        except:

            Enter()
            rprint("[bold red]ERROR : Invalid Details Entered.")
            Enter()

            wish = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if wish == 1:
                AddClass(cursor,connection,console)
            if wish == 2:
                return 0

def DisplayClass(cursor,console):
    def allClasses():

        Enter()
        cursor.execute("select * from Class")

        table = Table(title="Display All Classes")
        table.add_column("Class ID", style="cyan", no_wrap=True)
        table.add_column("Class", style="magenta")
        table.add_column("Division", style="magenta")
        table.add_column("Class Teacher", style="magenta")
        table.add_column("No: Of Students", style="magenta")
        table.add_column("Subject 1", style="magenta")
        table.add_column("Subject 2", style="magenta")
        table.add_column("Subject 3", style="magenta")
        table.add_column("Subject 4", style="magenta")
        table.add_column("Subject 5", style="magenta")
        for i in cursor:
            table.add_row(str(i[0]),str(i[1]),i[2],i[3],str(i[4]),i[5],i[6],i[7],i[8],i[9])
        console.print(table)

    def classWithTeacher():

        Enter()
        cursor.execute("select class,division,class_teacher from Class")

        table = Table(title="Display Class With Class Teacher")
        table.add_column("Class", style="magenta")
        table.add_column("Division", style="magenta")
        table.add_column("Class Teacher", style="magenta")
        for i in cursor:
            table.add_row(str(i[0]),i[1],i[2])
        console.print(table)


    def classWithStudent():

        Enter()
        cursor.execute("select class,division,no_of_students from Class")

        table = Table(title="Display Class With Number OF Students")
        table.add_column("Class", style="magenta")
        table.add_column("Division", style="magenta")
        table.add_column("Number OF Students", style="magenta")
        for i in cursor:
            table.add_row(str(i[0]),i[1],str(i[2]))
        console.print(table)


    while True:

        Enter()
        table = Table(title="Display Classes")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Display All Classes")
        table.add_row("2","Display Class With Class Teacher")
        table.add_row("3","Display Class With Number of Students")
        table.add_row("4","Back")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3,4)", [1, 2, 3, 4])

        if sectionValue == 1:
            allClasses()
        elif sectionValue == 2:
            classWithTeacher()
        elif sectionValue == 3:
            classWithStudent()
        else:
            break


def EditClass(cursor,connection,console):

    Enter()
    cursor.execute("select * from Class")

    table = Table(title="Display All Classes")
    table.add_column("Class ID", style="cyan", no_wrap=True)
    table.add_column("Class", style="magenta")
    table.add_column("Division", style="magenta")
    for i in cursor:
        table.add_row(str(i[0]),str(i[1]),i[2])
    console.print(table)
    
    classID = Checker("Enter the Class ID:", "int")
    Enter()
    classes = []
    cursor.execute("select * from Class")
    for i in cursor:
        classes.append(i[0])
    if classID in classes:
        EditClass2(classID,cursor,connection,console)
    else:
        rprint("[bold red]ERROR : Enter A Valid Class ID")
        Lag()
        return 0



def EditClass2(classID,cursor,connection,console):

    Enter()
    table = Table(title="Choose What to Edit")
    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Section", style="magenta")
    table.add_row("1","Class")
    table.add_row("2","Division")
    table.add_row("3","Class Teacher")
    table.add_row("4","Number Of Students")
    table.add_row("5","Subject 1")
    table.add_row("6","Subject 2")
    table.add_row("7","Subject 3")
    table.add_row("8","Subject 4")
    table.add_row("9","Subject 5")
    table.add_row("10","Exit")
    console.print(table)
    sectionValue = Choice("Enter Your Choice(1,2,3,4,5,6,7,8,9,10)", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    match sectionValue:
        case 1:
            value = Checker("Enter the Class (Max 2 Digits)", "int")
            sqlCol = 'class'
        case 2:
            rprint("\nEnter the Division(Max 3 Characters)")
            value = input(":")
            sqlCol = 'division'
        case 3:
            rprint("\nEnter the Class Teacher(Max 20 Characters)")
            value = input(":")
            sqlCol = 'class_teacher'
        case 4:
            value = Checker("Enter the No: of Students(Max 3 Digits)", "int")
            sqlCol = 'no_of_students'
        case 5:
            rprint("\nEnter the Subject 1(Max 20 Characters)")
            value = input(":")
            sqlCol = 'subject1'
        case 6:
            rprint("\nEnter the Subject 2(Max 20 Characters)")
            value = input(":")
            sqlCol = 'subject2'
        case 7:
            rprint("\nEnter the Subject 3(Max 20 Characters)")
            value = input(":")
            sqlCol = 'subject3'
        case 8:
            rprint("\nEnter the Subject 4(Max 20 Characters)")
            value = input(":")
            sqlCol = 'subject4'
        case 9:
            rprint("\nEnter the Subject 5(Max 20 Characters)")
            value = input(":")
            sqlCol = 'subject5'
        case 10:
            return 0
        
    try:
        if type(value) is int:
            query = f"update Class set {sqlCol}={value} where class_id={classID}"
            cursor.execute(query)
        else:
            query = f"update Class set {sqlCol}='{value}' where class_id={classID}"
            cursor.execute(query)
        connection.commit()

        Enter()
        with console.status("[bold green]Updating Details in Database...") as status:
            sleep(2)
            console.log(f'[bold][green]Class Updated Successfully.. ')
        Enter()
        Lag()
        Enter()

    except:

        Enter()
        rprint("[bold red]ERROR : Invalid Value Entered.")
        Enter()

        return 0



# Def17:REMOVE CLASS MENU
def RemoveClass(mycursor,lib):
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