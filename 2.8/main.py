hoursWorked = float(input("Please Enter The Number Of Hours You Worked This Week: "))
hourlyRate = float(input("Please Enter Your Hourly Rate: "))

if hoursWorked < 70:
    grossIncome = hourlyRate * hoursWorked
    overtimeIncome = (hoursWorked - 35) * 1.5

    grossEarningsSTR = str(grossIncome)
    overtimeEarningsSTR = int(overtimeIncome)

    if overtimeEarningsSTR <= 0:
        overtimeEarningsSTR = 0
    else:
        print("Error...")

    print("You Earned A Total Of £", grossEarningsSTR)
    print("You Earned A Total Of £", overtimeEarningsSTR)

else:
    print("You can't work that many hours a week!")
