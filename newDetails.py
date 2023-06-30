def addDetails(filename):
    flag=input("do u want to add more details in file:y/n")
    while(flag=="y"):
        name=input("whats name : ")
        dep = input("whats department he/she belong : ")
        sal =input("what is his/her salary :")
        data=name+","+dep+","+sal
        file=open(filename, "a")
        file.write("\n"+data)
        flag=input("do u want to add more details in file:y/n")
