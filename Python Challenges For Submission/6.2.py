# Created & Programmed By: Modifier20

import random
numberArray = []
itteration = 0

# THIS CALCULATES AND PRINTS OUT THE AVERAGE OF THE RANDOMLY GENERATED NUMBERS
def average():
    numberArrayAverage = sum(numberArray) / len(numberArray)
    print(numberArrayAverage)

# RANDOM NUMBER ARRAY GENERATION
randomNumberOne = random.randint(1,25)
while randomNumberOne >= itteration:
    itteration = itteration + 1
    randomArrayNumberGenneration = random.randint(1,25)
    additionToArray = numberArray.append(randomArrayNumberGenneration)

average()
