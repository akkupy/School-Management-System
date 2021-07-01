# Def1:SPACE
def Enter():
    print()


# Def2:HORIZONTAL LINE
def Star():
    print('=' * 121)


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