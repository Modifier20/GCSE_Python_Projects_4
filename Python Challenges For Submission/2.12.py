# Created By: Modifier20
# On: Fri 5th Feb - 14:38

monthNum = int(input("Please Enter The Number of a Month: "))
year = int(input("Please Enter A Year: "))

# CALCULATES IF THE YEAR IS A LEAP YEAR
if year / 4:
    print("The Year is a leap year")
else:
    print("It is not a leap year")
if monthNum == 1:
    print("There are 31 Day's in January")
elif monthNum == 2:
    print("There are 28 Day's in February\nThere Are 29 in a leap year")
elif monthNum == 3:
    print("There are 31 Day's in March")
elif monthNum == 4:
    print("There are 30 Day's in April")
elif monthNum == 5:
    print("There are 31 Day's in May")
elif monthNum == 6:
    print("There are 30 Day's in June")
elif monthNum == 7:
    print("There are 31 Day's in July")
elif monthNum == 8:
    print("There are 31 Day's in August")
elif monthNum == 9:
    print("There are 30 Day's in September")
elif monthNum == 10:
    print("There are 31 Day's in October")
elif monthNum == 11:
    print("There are 30 Day's in November")
elif monthNum == 12:
    print("There are 31 Day's in December")
else:
    print("This isn't a valid month number...")


