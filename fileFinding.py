import os.path
def fileExistOrNot(filename):
    path = "./"+filename
    print(path)
    check_file = os.path.isfile(path)
    if(check_file==True):
        return True
