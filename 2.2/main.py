num01 = int(input("Please Enter The First Number>"))
num02 = int(input("Please Enter The Second Number>"))

if num01 > num02:
    print(num01, "is bigger than", num02)
elif num01 < num02:
    print(num02, "is bigger than", num01)
elif num01 == num02:
    print(num01, "is equal to", num02)
else:
    print("Unvalid Chars Have Been Entered.")