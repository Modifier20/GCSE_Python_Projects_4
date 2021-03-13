def takenNumber():
    global largestValue

    numberOne = int(input("Please Enter Your First Number... "))
    numberTwo = int(input("Please Enter Your Second Number... "))
    numberThree = int(input("Please Enter Your Third Number... "))

    if numberOne > numberTwo and numberThree:
        if numberThree > numberOne and numberTwo:
            largestValue = numberThree
            print("The largest value", numberThree)
        else:
            largestValue = numberTwo
            print("The largest value", numberOne)

    else:
        largestValue = numberTwo
        print("The largest value", numberTwo)

takenNumber()