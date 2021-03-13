# Created & Programmed By: Modifier20

def countdown():
    usersInteger = int(input("Please enter a number to count down from: "))
    print(usersInteger)
    while usersInteger > 0:
        usersInteger = usersInteger - 1
        print(usersInteger)

countdown()
