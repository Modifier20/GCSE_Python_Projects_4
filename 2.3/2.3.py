# Created By: Modifier20
# On: Fri 26nd Jan - 09:02

num01 = int(input("Number 1>"))
num02 = int(input("Number 2>"))
num03 = int(input("Number 3>"))

if num01 > num02:
    if num01 > num03:
        print("The Highest Number Was", num01)
    else:
        print("The Highest Number Was", num03)
else:
    if num02 > num03:
        print("The Highest Number Was", num02)
    else:
        print("The Highest Number Was", num03)


