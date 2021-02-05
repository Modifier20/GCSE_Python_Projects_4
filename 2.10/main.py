percentage = int(input("Please Enter A Percentage: "))

if percentage <= 39:
    print("You Achieved A Grade: E")
elif (percentage >= 40) and (percentage <= 45):
    print('You Achieved A Grade: D')
elif (percentage >= 46) and (percentage <= 55):
    print('You Achieved A Grade: C')
elif (percentage >= 56) and (percentage <= 65):
    print('You Achieved A Grade: B')
elif (percentage >= 66) and (percentage <= 75):
    print('Wow That Is Good. You Achieved A Grade: A')
elif (percentage >= 76) and (percentage <= 100):
    print('Wow That Is Amazing. You Achieved A Grade: A*')
else:
    print("That is not a valid percentage!")
