# SCHOOL MANAGEMENT SYSTEM...


import sys
import mysql.connector as msc
import Modules



print(r'''
     __       _       _           
    /  \     | |     | | 
   /    \    | | /\  | | /\   _   _
  /  /\  \   | |/ /  | |/ /  | | | |  
 /  ____  \  | |\ \  | |\ \  | |_| |
/__/    \__\ |_| \_\ |_| \_\  \___/  ''')
print("\n*************************************")
print("\n* Copyright of Akash, 2021          *")
print("\n* https://www.github.com/akkupy     *")
print("\n* https://t.me/akkupy               *")
print("\n*************************************")
Modules.Enter()






def main():
    Modules.Enter()
    Modules.Star()
    print("\t\t\t\tWELCOME TO SCHOOL MANAGEMENT SYSTEM")
    Modules.Star()
    Modules.Enter()
    print("ENTER THE PASSWORD TO ACCESS DATABASE")
    a = input(':')
    Modules.Enter()
    print("RE-ENTER THE PASSWORD")
    b = input(':')
    Modules.Enter()
    y = ''
    if a == b:
        y = a
    else:
        Modules.Enter()
        print("PASSWORD MISMATCH!")
        sys.exit()
    Modules.Enter()
    v = Modules.Choice("CREATE NEW DATABASE/USE EXISTING(1,2):", [1, 2])
    if v == 2:
        r = Modules.list_database(y)
        Modules.Enter()
        z = input("\tEnter The DataBase Name:")
        if z in r:
            Modules.Enter()
            print("\tDATABASE CHANGED")
            Modules.Enter()
            Modules.Lag()
        else:
            Modules.Enter()
            print("ENTER A VALID DATABASE OR CREATE A NEW ONE")
            sys.exit()
        Modules.Enter()

    if v == 1:
        z = Modules.create_database(y)
        Modules.create_table(y,z)

    lib = msc.connect(host="localhost", user="root", passwd=y, database=z)
    mycursor = lib.cursor()
    while True:
        Modules.Enter()
        Modules.Star()
        Modules.Enter()
        print("\t\t\t SCHOOL NAME WITH PLACE")
        print("\t\t\t ********************************")
        Modules.Enter()
        print("\t\t 1.STUDENTS")
        print("\t\t 2.TEACHERS")
        print("\t\t 3.CLASSES")
        print("\t\t 4.EXIT")
        Modules.Enter()
        m = Modules.Choice("\tEnter a Choice(1,2,3,4):", [1, 2, 3, 4])
        # STUDENTS
        if m == 1:
            # Def3
            Modules.Student(mycursor,lib)
        # TEACHERS
        elif m == 2:
            # Def4
            Modules.Teachers(mycursor,lib)
        # CLASS
        elif m == 3:
            # Def5
            Modules.Class(mycursor,lib)
        # EXIT
        elif m == 4:
            Modules.Enter()
            print("DATABASE CLOSED")
            Modules.Enter()
            print("PROGRAM CLOSED")
            Modules.Enter()
            Modules.Lag()
            Modules.Enter()
            break

    
if __name__=="__main__":
    main()