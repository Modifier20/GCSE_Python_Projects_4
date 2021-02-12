repeat = "false"
sumNumber = 0

import array

arr1 = array.array('i', [1, 2, 3])

while repeat != "true":
    number = int(input("Number> "))
    if number != 0:
        sumNumber = sumNumber + number
        array.insert(array)
    else:
        print(array)
        #print("Your Final Number is:", sumNumber)
        break
