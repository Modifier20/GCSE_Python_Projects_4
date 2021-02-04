temperature = int(input("Please Enter A Temperature: "))

FREEZING = 0
NORMAL = 1
BOILING = 100

if temperature <= 0:
    print("Your Water Is Freezing!")
elif temperature >= 1:
    if temperature >= 100:
        print("Your Water Is Boiling!")
    else:
        print("Your Water Is Normal!")
else:
    print("Invalid Character's Have Been Entered")

