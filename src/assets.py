from rich import print as rprint

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


# Choice Picker
def Choice(inputString: str, inputRange: list):
    try:
        Enter()
        rprint(inputString)
        inputChoice = int(input(':'))
        if inputChoice in inputRange:
            return inputChoice
        else:
            Enter()
            rprint(f"[bold red]ERROR : Enter the choice from {inputRange}")
            return Choice(inputString, inputRange)
    except:
        Enter()
        rprint(f"[bold red]ERROR : Enter the choice from {inputRange}")
        return Choice(inputString, inputRange)