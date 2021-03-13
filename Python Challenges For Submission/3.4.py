total = 0
numberToAdd = 1

while numberToAdd != 0:
    numberToAdd = int(input("Enter A Number To Add: "))
    total = numberToAdd + total
    print("|-- YOUR CURRENT TOTAL IS --|")
    print("|--", total)
    print("   ")