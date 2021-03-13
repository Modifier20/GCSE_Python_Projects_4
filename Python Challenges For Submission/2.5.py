# Created & Programmed By: Modifier20

import random

num01 = 100
num02 = 75
num03 = 50

if num01 > num02:
    if num01 > num03:
        print("The Highest Number Was", num01)
    else:
        print("The Highest Number Was", num03)
else:
    if num02 > num03:
        print("The Highest Number Was", num02)
    else:
        print("The Highest Number Was", num03)

print("------------------------------------------------------------------------------")

#USE'S THE RANDOM MODULE TO GENERATE A RANDOM NUMBER
print("USE'S THE RANDOM MODULE TO GENERATE A RANDOM NUMBER")

number01 = random.randint(1,100)
number02 = random.randint(1,100)
number03 = random.randint(1,100)

if number01 > number02:
    if number01 > number03:
        print("The Highest Number Was (Number01)", number01)
    else:
        print("The Highest Number Was (Number03)", number03)
else:
    if number02 > number03:
        print("The Highest Number Was (Number02)", number02)
    else:
        print("The Highest Number Was (Number03)", number03)
