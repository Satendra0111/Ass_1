def displayDetails(filename):
    print("*********Here all details **************")
    file= open(filename, "r")
    data = file.read()
    print(data)
