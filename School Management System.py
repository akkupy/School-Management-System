# SCHOOL MANAGEMENT SYSTEM


import sys
import mysql.connector as msc
import Modules.classes
import Modules.mysql_database
import Modules.student
import Modules.teacher
import Modules.assets




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
    z = Modules.mysql_database.create_database()
    Modules.mysql_database.create_table()

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
