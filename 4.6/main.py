import random

randomNumber = random.randint(1, 100)
guess = 0

while guess != randomNumber:
    guess = int(input("Please Guess The Number I Have Though Of? "))
    if randomNumber > guess:
        print("Too Small Try Again...\n")
    elif randomNumber < guess:
        print("Too High Try Again...\n")
else:
    print("Well Done You Guessed Correctly...")
