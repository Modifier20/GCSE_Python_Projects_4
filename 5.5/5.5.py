StudentName = [["James", "Jill", "Jack", "Sophie", "Henry", "Angus"],
               ["02.05.1990", "20.12.2012", "01.01.1985", "08.08.1988", "28.02.2000", "05.02.2021"]]

print("STUDENT NAME(S): James, Jill, Jack, Sophine, Henry, Angus")
StudentDataRequest = input("Please Enter The Student's Name: ")

if StudentDataRequest == StudentName[0][0]:
    print(StudentName[1][0])
elif StudentDataRequest == StudentName[0][1]:
    print(StudentName[1][1])
elif StudentDataRequest == StudentName[0][2]:
    print(StudentName[1][2])
elif StudentDataRequest == StudentName[0][3]:
    print(StudentName[1][3])
elif StudentDataRequest == StudentName[0][4]:
    print(StudentName[1][4])
elif StudentDataRequest == StudentName[0][5]:
    print(StudentName[1][5])
else:
    print("Invalid Input...")