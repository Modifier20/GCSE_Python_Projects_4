recordWriting = open("names.txt", "a")

# THIS TAKES IN THE USERS INPUT FOR THE RECORDS
recordNumber = input("Record number(rr): ")
firstnameOfStudent = input("Firstname: ")
surnameOfStudent = input("Surname: ")
mark = input("Mark(mm%): ")

# THIS TAKES THE USER INPUT AND FORMATS IT FOR THE TEXT FILE
recordNoEntry = "Record Number:", recordNumber, " "
firstNameEntry = "First Name:", firstnameOfStudent, " "
surnameEntry = "Surname:", surnameOfStudent, " "
markEntry = "Mark:", mark, "\n"

# THIS SECTION OF CODE CONVERTS IT TO STR FOR WRITING TO FILE
recordNoEntryStr = str(recordNoEntry)
firstNameEntryStr = str(firstNameEntry)
surnameEntryStr = str(surnameEntry)
markEntryStr = str(markEntry)

# THIS WRITES ALL OF THE USERS ENTRIES INTO THE TEXT FILE
recordWriting.write(recordNoEntryStr)
recordWriting.write(firstNameEntryStr)
recordWriting.write(surnameEntryStr)
recordWriting.write(markEntryStr)
recordWriting.close()