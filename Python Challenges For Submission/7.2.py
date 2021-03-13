# Created & Programmed By: Modifier20

usernamesAndPass = 'usersData.txt'
with open(usernamesAndPass) as f_obj:
    usernamesData = f_obj.read()

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
    print("We're very sorry but" + name + "is not recognised in the system.\nYou may want to cosider ding an internet to find a solution.")
