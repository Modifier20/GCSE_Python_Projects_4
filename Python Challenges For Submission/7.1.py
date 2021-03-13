# Created & Programmed By: Modifier20

itteration = 0

while itteration != 5:
    enteredName = str(input("Please Enter A Name> "))

    file = open("names.txt", "a")
    file.write(enteredName)
    file.close()
    itteration = itteration + 1

nameFile = open("names.txt", "r")
printEnteredNames = nameFile.readline()
print(printEnteredNames)
nameFile.close()
