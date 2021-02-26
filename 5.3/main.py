import random

itteration = 1
dieRolls = []

while itteration <= 29:
    randomNumber = random.randint(1,6)
    dieRolls.append(randomNumber)
    itteration = itteration + 1

print(" ")
print(dieRolls)
print("|----------------------|")
print("|    VALUE'S NAMED     |")
print("|----------------------|")
print("| The Number of 6s:", dieRolls.count(6), " |")
print("| The Number of 5s:", dieRolls.count(5), " |")
print("| The Number of 4s:", dieRolls.count(4), " |")
print("| The Number of 3s:", dieRolls.count(3), " |")
print("| The Number of 2s:", dieRolls.count(2), " |")
print("| The Number of 1s:", dieRolls.count(1), " |")
print("|----------------------|")