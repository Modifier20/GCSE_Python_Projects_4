def takenNumber():
    global largestValue

    numberOne = int(input("Please Enter Your First Number... "))
    numberTwo = int(input("Please Enter Your Second Number... "))
    numberThree = int(input("Please Enter Your Third Number... "))

    if numberOne > numberTwo and numberThree:
        largestValue = numberOne
        print("The largest value", numberOne)
    elif numberTwo > numberOne and numberThree:
        largestValue = numberTwo
        print("The largest value", numberTwo)
    # THIS IS THE PROBLEMATIC CODE #####################
    elif numberThree < numberOne and numberTwo:
        largestValue = numberThree
    ####################################################
    else:
        print("The largest value", numberTwo)

takenNumber()