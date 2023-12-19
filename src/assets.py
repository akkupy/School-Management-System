from rich import print as rprint

# Def1:SPACE
def Enter():
    print()


# Def2:HORIZONTAL LINE
def Star():
    print('=' * 121)


# Def21:ENTER KEY FUNCTION
def Lag():
    rprint("Press ENTER KEY to Continue")
    input("")


# Def22:INTEGER RETREIVAL CHECKING
def Checker(inputString: str, type: str = 'foo'):
    if type == "int":
        try:
            Enter()
            rprint(inputString)
            userInput = int(input(':'))
            return userInput
        except:
            Enter()
            rprint("[bold red]ERROR : Enter As per Instruction")
            return Checker(inputString, type)


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