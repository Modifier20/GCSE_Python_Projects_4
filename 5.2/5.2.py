nameList = []
itteration = 0

while (itteration != 6):
    nameInput = input("Please Enter A Name For The List: ")
    nameList.append(nameInput)
    itteration = itteration + 1

nameList.reverse()
print(nameList)