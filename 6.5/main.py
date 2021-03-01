import random
guessStatus = False

# RANDOMLY GENERATED NUMBERS.
def computersGuess():
    generatedGuess = random.randint(1,50)
    return generatedGuess

# GUESSING PROGRAM
computersGuess()
while guessStatus != True:
    computersGuess()



    # THIS SECTION CHECKS TO SEE IF THE CORRECT GUESS IS TRUE OR FALSE
    if guessStatus == False:
        higherOrLower = input("Is it Higher or Lower> ")
        if higherOrLower == "higher":
            computersGuess()
        elif higherOrLower == "Higher":
            computersGuess()
            
    elif guessStatus == True:
