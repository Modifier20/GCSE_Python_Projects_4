# THIS TAKES THE USER'S INPUT OF THEIR DATE OF BIRTH
day = int(input("Please enter the year of your birth(dd): "))
month = int(input("Please enter the month of your birth(mm): "))
year = int(input("Please enter the year of your birth(yyyy): "))

# ADD'S ONE TO THE DAY AND MOVES IT ON
if day < 31:
    day = day + 1
    print(day, month, year)
elif day >= 31:
    month = month + 1
    day = 1
    print(day, month, year)
else:
    print("You have not entered a valid date. Please restart and try again.")