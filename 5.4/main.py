import random
lotteryNumber = []
itteration = 0

while itteration != 6:
    randomLotteryNumber = random.randint(1, 49)
    if randomLotteryNumber in lotteryNumber:
        print()
    else:
        lotteryNumber.append(randomLotteryNumber)
        itteration = itteration + 1

print("You Lottery Number's Are: ", lotteryNumber)