# Created & Programmed By: Modifier20

def login():
    # THIS IS THE USERS INPUT FOR THE USER NAME
    name = input("Enter a username: ")

    # THIS WILL DETERMINE WHETHER THE USERNAME IS FOUND IN THE USERS DATA FILE
    if name in usernamesData:
        password = input("Please enter your password... ")

        # THIS WILL DETERMINE WHETHER THE PASSWORD IS FOUND IN THE USERS DATA FILE
        if password in usernamesData:
            print("Welcome " + name + " please remember to log out of your session when you are done...")

        # THIS IS THE ERROR MESSAGE FOR WHEN THE PASSWORD IS NOT RECOGNISED.
        else:
            print("We're very sorry but your password has not recognised in the system.\nYou may want to cosider ding an internet to find a solution.")

    # THIS IS THE ERROR MESSAGE FOR A FAILED USERNAME
    else:
        print("We're very sorry but " + name + " is not recognised in the system.\nYou may want to cosider ding an internet to find a solution.")

def addUserOrChangeUsers():
    usernamesAndPassAppend = open("usersData.txt", "wt")

    print("Welcome. You Are Here Because You Want To Change You User Name.")
    currentUser = str(input("What is Your Current User Name> "))
    if currentUser in usernamesData:
        currentPassword = str(input("What is your current password> "))
        if currentPassword in usernamesData:

            # THIS TAKES IN THE NEW USERNAME AND PASSWORD
            appendedUser = str(input("What Do You Want Your New User To Be Called> "))
            appendedPass = str(input("What is Your New Password> "))

            # THIS ADDS THE NEW USER TO THE TEXT FILE
            usernamesAndPassAppend.write(appendedUser + "\n" + appendedPass)

            # THIS REMOVES THE OLD USER FROM THE TEXT FILE
            usernamesAndPassAppend.write(appendedUser.replace(appendedUser, ''))
            usernamesAndPassAppend.write(appendedPass.replace(appendedPass, ''))
            #usernamesAndPassAppend = usernamesAndPassAppend.truncate(currentUser)
            #usernamesAndPassAppend = usernamesAndPassAppend.truncate(currentPassword)

#
#
#
# CURRENTLY THE ONLY ISSUE I AM SUFFERING WITH IS THAT IT REPLACES ALLL OF THE USERNAMES AND PASSWORDS IN THE TEXT FILE WHEN YOU TRY TO JUST REMOVE ONE LINE
#
#
#

usernamesAndPass = 'usersData.txt'
with open(usernamesAndPass) as f_obj:
    usernamesData = f_obj.read()
print("Welcome...")
print()
option = input ("What Can We Do For You?\n1) Login to Our System\n2) Change or Add User\nSYSTEM(1,2)> ")
if option == "1":
    login()
elif option == "2":
    addUserOrChangeUsers()
    login()
else:
    print("Please Enter A Valid Option When You Restart The Program.")
