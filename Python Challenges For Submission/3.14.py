# Created & Programmed By: Modifier20

zero = 0
usersNumber = int(input("Please enter a number you want the primes up to: "))
for number in range(zero, usersNumber + 1):
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)
