numberArray = []

# THIS TAKES IN THE USERS NUMBER INPUTS, AND ADDS THEM TO THE ARRAY TO BE AVERAGED
def numberInput():
    itteration = 0
    while itteration <= 10:
        itteration = itteration + 1
        numberInput = int(input("Enter A Number> "))
        addToNumberArray = numberArray.append(numberInput)

# THIS CALCULATES AND PRINTS OUT THE AVERAGE OF THE RANDOMLY GENERATED NUMBERS
def average():
    numberArrayAverage = sum(numberArray) / len(numberArray)
    print(numberArrayAverage)

# THIS RUNS THE FUNCTIONS
numberInput()
average()