def caesar(realText, step):
    outText = []
    encryptedText = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for eachLetter in realText:
        # THIS SECTION OF THE CODE ADS THE CIPHER TO THE UPPERCASE LETTERS.
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            encryptedText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)

        # THIS SECTION OF THE CODE ADS THE CIPHER TO THE LOWERCASE LETTERS.
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            encryptedText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)

        # THIS SECTION OF THE CODE ADS THE CIPHER TO THE NUMBERS.
        elif eachLetter in numbers:
            index = numbers.index(eachLetter)
            crypting = (index + step) % 26
            encryptedText.append(crypting)
            newLetter = numbers[crypting]
            outText.append(newLetter)
    return outText


#password = input("Password... ")
#code = caesar(password, 2)
#print()
#print(code)
#print()

def login():
    # THIS IS THE USERS INPUT FOR THE USER NAME
    name = input("Enter a username: ")

    # THIS WILL DETERMINE WHETHER THE USERNAME IS FOUND IN THE USERS DATA FILE
    if name in usernamesData:
        password = input("Please enter your password... ")
        encryptedPassword = caesar(password, 2)
        stringEncryptedPassword = str(encryptedPassword)
        print(stringEncryptedPassword)

        # THIS WILL DETERMINE WHETHER THE PASSWORD IS FOUND IN THE USERS DATA FILE
        if stringEncryptedPassword in usernamesData:
            print("Welcome " + name + " please remember to log out of your session when you are done...")

        # THIS IS THE ERROR MESSAGE FOR WHEN THE PASSWORD IS NOT RECOGNISED.
        else:
            print("We're very sorry but your password has not recognised in the system.\nYou may want to cosider ding an internet to find a solution.")

    # THIS IS THE ERROR MESSAGE FOR A FAILED USERNAME
    else:
        print("We're very sorry but " + name + " is not recognised in the system.\nYou may want to cosider ding an internet to find a solution.")

#def addUserOrChangeUsers():
#    usernamesAndPassAppend = open("usersData.txt", "wt")
#
#    print("Welcome. You Are Here Because You Want To Change You User Name.")
#    currentUser = str(input("What is Your Current User Name> "))
#    if currentUser in usernamesData:
#        currentPassword = str(input("What is your current password> "))
#        if currentPassword in usernamesData:
#
#            # THIS TAKES IN THE NEW USERNAME AND PASSWORD
#            appendedUser = str(input("What Do You Want Your New User To Be Called> "))
#            appendedPass = str(input("What is Your New Password> "))
#
#            # THIS ADDS THE NEW USER TO THE TEXT FILE
#            usernamesAndPassAppend.write(appendedUser + "\n" + appendedPass)
#
            # THIS REMOVES THE OLD USER FROM THE TEXT FILE
#            usernamesAndPassAppend.write(appendedUser.replace(appendedUser, ''))
#            usernamesAndPassAppend.write(appendedPass.replace(appendedPass, ''))
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
login()
