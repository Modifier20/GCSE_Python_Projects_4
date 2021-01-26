# Created By: Modifier20
# On: Fri 26nd Jan - 09:02

num01 = int(input("Number 1>"))
num02 = int(input("Number 2>"))
num03 = int(input("Number 3>"))

if num01 > num02 and num03:
    print(num01, "is the largest number.")
elif num02 > num01 and num03:
    print(num02, "is the largest number.")
elif num03 > num02 and num01:
    print(num03, "is the largest number.")
#elif num01 < num02 and num03:
#    print("Worked")
#elif num02 < num01 and num03:
#    print("Worked")
#elif num03 < num02 and num01:
#    print("Worked")
else:
    print("Invalid Chars")
