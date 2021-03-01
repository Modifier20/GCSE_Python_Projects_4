import random

# RANDOM NUMBER ARRAY GENERATION
numberArray = []
itteration = 0
randomNumberOne = random.randint(1,25)
while randomNumberOne >= itteration:
    itteration = itteration + 1
    randomArrayNumberGenneration = random.randint(1,25)
    additionToArray = numberArray.append(randomArrayNumberGenneration)

# THIS PRINTS THE AVERAGE OF THE NUMBER ARRAY
numberArrayAverage = sum(numberArray) / len(numberArray)
print(numberArrayAverage)
