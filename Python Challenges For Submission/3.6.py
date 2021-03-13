# Created & Programmed By: Modifier20

# THIS IS THE VARIABLE
total = 0
average = 0
numberToAdd = 1
enteredNumbersArray = []

while numberToAdd != 0:
    # THIS IS WHERE THE USERS INPUT IT TAKEN IN.
    numberToAdd = int(input("Enter A Number To Add: "))

    # THIS IS WHERE THE MATHMATICS IS DONE AND THINGS ARE ADDED TO ARRAY'S.
    enteredNumbersArray.append(numberToAdd)
    total = numberToAdd + total
    average = sum(enteredNumbersArray) / len(enteredNumbersArray)

    # THIS PRINT'S OUT THE TOTALS AND AVERAGES OF THE NUMBERS THAT HAVE BEEN ENTERED.
    print("|-- YOUR CURRENT TOTAL IS --|")
    print("|--", total)

    print("|-- YOUR CURRENT AVERAGE IS --|")
    print("|--", average)
    print("   ")
