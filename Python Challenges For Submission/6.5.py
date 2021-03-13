import random
attempts = 0
ansStatus = False

# THIS TAKES IN THE USERS RANGE INTO THE PROGRAM
usersRange = int(input("Please Enter A Number For The Range> "))

# THIS WILL GENERATE A RANDOM NUMBER FROM ZERO TO THE USERS RANGE
def computerGeneratedGuess():
    global computersGuess
    global prevGuess
    computersGuess = random.randint(0, usersRange)
    prevGuess = computersGuess
    return computersGuess + prevGuess

# THIS GENERATES THE COMPUTERS HIGHER GUESS
def higherComputerGeneratedGuess():
    global computersGuess
    global prevGuess
    computersGuess = random.randint(prevGuess, usersRange)
    prevGuess = computersGuess
    return computersGuess + prevGuess

# THIS GENERATES THE COMPUTERS LOWER GUESS
def lowerComputerGeneratedGuess():
    global computersGuess
    global prevGuess
    computersGuess = random.randint(0, prevGuess)
    prevGuess = computersGuess
    return computersGuess + prevGuess

# THIS IS THE TRUE OF FALSE CODE
def trueOrFalse():
    global ansStatus
    ansStatus = input("Did I Guess Correctly> ")
    return ansStatus

computerGeneratedGuess()

while ansStatus != True:
    print(computersGuess)
    trueOrFalse()

    #THIS PRINTS THE CONGRATULATIONS SENTENCE(S) AT THE END OF THE SCRIPT
    if ansStatus == True:
        print("\nThat's Amazing, I Haven't Played This Before...\nGoodbye, and have a good day.")
        print("It Took Me", attempts, "Attempts...")

    else:
        # THIS RUNS DIRECTS THE HIGHER OR LOWERE ENTRIES TO THE CORRECT FUNCTION AND ADD ONE TO THE ATTEMPTS SCORE.
        attempts = attempts + 1
        higherOrLower = input("Higher(H) or Lower(L) Then? ")
        if higherOrLower == "H":
            higherComputerGeneratedGuess()
        elif higherOrLower == "h":
            higherComputerGeneratedGuess()
        elif higherOrLower == "L":
            lowerComputerGeneratedGuess()
        elif higherOrLower == "l":
            lowerComputerGeneratedGuess()
        else:
            print("Invalid Input")
