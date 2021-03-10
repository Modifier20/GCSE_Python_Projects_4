# ENTER A NUMBER TO BE SQUARED
number = int(input("Enter A Number"))

# ARRAY OF NUMBER
squaresArray = []

# THIS WILL REPEAT THE PROCESS THE NUMBER ENTERED AND IT WILL SQUARE THAT NUMBER
while number > 0:
    square = number ** 2
    squaresArray.append(square)
    number = number - 1

# THIS PRINTS OUT ALL OF THE SQUARES BETWEEN THE NUMBER ENTERED AND ONE
print(squaresArray)
