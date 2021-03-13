import random
import os

print()
print("PROGRAM 5.4a RUNNING...")
print()

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

print()
print("PROGRAM 5.4b RUNNING...")
print()

StudentName = ["James", "Jill", "Jack", "Sophie", "Henry", "Angus"]
DOB = ["02.05.1990", "20.12.2012", "01.01.1985", "08.08.1988", "28.02.2000", "05.02.2021"]

print("STUDENT NAME(S):", StudentName)
StudentDataRequest = input("Please Enter The Student's Name: ")

if StudentName.index(StudentDataRequest) == 0:
    print("Born:", DOB[0])
elif StudentName.index(StudentDataRequest) == 1:
    print("Born:", DOB[1])
elif StudentName.index(StudentDataRequest) == 2:
    print("Born:", DOB[2])
elif StudentName.index(StudentDataRequest) == 3:
    print("Born:", DOB[3])
elif StudentName.index(StudentDataRequest) == 4:
    print("Born:", DOB[4])
elif StudentName.index(StudentDataRequest) == 5:
    print("Born:", DOB[5])
else:
    print("Invalid Input...")