number01 = int(input("Number 1> "))
number02 = int(input("Number 2> "))
number03 = int(input("Number 3> "))

if (number01 > number02) and (number01 > number03):
    print("The Highest Value Was 1")
else:
    if (number02 > number03) and (number02 > number01):
        print("The Highest Value Was 2")
    else:
        print("The Highest Value Was 3")