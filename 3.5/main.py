# Write a program that asks the user for a number between 10 and 30 inclusive and will
# validate, that is test, the input.  It should repeatedly ask the user for this number
# until the input is within the valid range.



value = input("Please Enter A Number Between 10 and 30")
if (value > 10) or (value == 10):
    print("Print Your Value Was Within The Range!")
elif (value < 30) or (value == 30):
    print("Print Your Value Was Within The Range!")
elif value < 10:
    print("Your Value Was Out of Range")
elif value > 30:
    print("Your Value Was Out of Range")
else:
    print("This is not a valid number!")
