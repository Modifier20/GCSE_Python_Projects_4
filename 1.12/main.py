value = int(input("Please Enter A Value: £"))

print ("Twenties: " + str((value // 20)))
print ("Tens: " + str((value % 20) // 10))
print ("Fives: " + str(((value % 20)  % 10) // 5))
print ("Twos: " + str((((value % 20)  % 10) % 5) // 2))
print ("Ones: " + str((((value % 20)  % 10) % 5) % 2))