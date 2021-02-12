repeat = "false"
sumNumber = 0

while repeat != "true":
    number = int(input("Number> "))
    if number != 0:
        sumNumber = sumNumber + number
    else:
        print("Your Final Number is:", sumNumber)
        break
