day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

printMonth = "none"

if month == 1:
    printMonth = "January"
elif month == 2:
    printMonth = "February"
elif month == 3:
    printMonth = "March"
elif month == 4:
    printMonth = "April"
elif month == 5:
    printMonth = "May"
elif month == 6:
    printMonth = "June"
elif month == 7:
    printMonth = "July"
elif month == 8:
    printMonth = "August"
elif month == 9:
    printMonth = "September"
elif month == 10:
    printMonth = "October"
elif month == 11:
    printMonth = "Novemeber"
elif month == 12:
    printMonth = "December"

print(day, printMonth, year)