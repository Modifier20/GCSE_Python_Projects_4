def takenNumber():
    global largestValue
    numberOne = int(input("Please Enter Your First Number... "))
    numberTwo = int(input("Please Enter Your Second Number... "))
    numberThree = int(input("Please Enter Your Third Number... "))
    if numberOne > numberTwo and numberThree:
        largestValue = numberOne
    elif numberTwo > numberOne and numberThree:
        largestValue = numberTwo
    elif numberThree > numberTwo and numberOne:
        largestValue = numberThree
    else:
        print("No Valid Answers Were Given")
    return largestValue

takenNumber()
print(largestValue)