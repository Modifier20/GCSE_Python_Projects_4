def takenNumber():
    global largestValue

    numberOne = int(input("Please Enter Your First Number... "))
    numberTwo = int(input("Please Enter Your Second Number... "))
    numberThree = int(input("Please Enter Your Third Number... "))

    if numberOne > numberTwo and numberThree:
        largestValue = numberOne
    elif numberTwo > numberOne and numberThree:
        largestValue = numberTwo
    # THIS IS THE PROBLEMATIC CODE #####################
    elif numberThree and numberTwo < numberThree:
        largestValue = numberThree
    ####################################################

    else:
        print("Invalid Answer...")
    return largestValue

takenNumber()
print(largestValue)