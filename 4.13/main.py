import time

#
#
#
# THIS PROGRAM CURRENTLY TElLS ME HOW OLD I AM GOING TO BE IN THIS YEAR, SOMETHING TO COMEBACK AND THINK ABOUT
#
#
#

Day = int(input("Please Enter The Day You Were Born (dd)> "))
Month = int(input("Please Enter The Month You Were Born (mm)> "))
Year = int(input("Please Enter The Year You Were Born (yy)"))

d = Day
m = Month
y = Year
current = time.strftime("%y")
currentYear = int(current)
yearsAlive = currentYear - y

print("You Are ", yearsAlive, " Old.")