import datetime

# THIS TAKES IN THE USERS INPUT OF BIRTH YEAR, AND CALCULATES THE CURRENT YEAR.
yearOfBirth = int(input("Enter your year of birth: "))
currentYear = datetime.date.today().year

# THIS CALCULATES YOUR CURRENT AGE BASED OFF THE USERS INPUTTED AGE, AND THE CALCULATED CURRENT YEAR
ageYear = currentYear - yearOfBirth

# THIS PRINTS OUT YOUR AGE
print("Your currently", ageYear, "years of age.")