# Created & Programmed By: Modifier20

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

enteredNumber = int(input("Please Enter The Month Number (0-11): "))

if enteredNumber != (1 <= 12):
    print(month[enteredNumber])
else:
    print("You Haven't Entered A Valid Month Number.")
