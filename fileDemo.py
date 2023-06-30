from fileFinding import fileExistOrNot
from newDetails import addDetails
from displayFile import displayDetails

fileName=input("Enter the file name with extension  : ")
exit=fileExistOrNot(fileName)
print(exit)
if(exit==True):
    print("File already exist")
    addDetails(fileName)
    displayDetails(fileName)
else:
        print("file not exist")