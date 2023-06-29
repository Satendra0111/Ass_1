
def walkThrough(countA, countB):
    print("=====================================")
    for i in range (1,31,1):
        if i<10:
            i=str(i).zfill(2)
            if int(i)==countA:
                print ("A", "|", end=" ")
            elif int(i)==countB:
                print ("B", "|", end=" ") 
            else:
                print (i, "|", end=" ")
            i=int(i)
        else:
            if i==countA:
                print ("A", "|", end=" ")
            elif i==countB:
                print ("B", "|", end=" ") 
            else:
                print (i, "|", end=" ")
        if i%5 ==0:
            print("\n")
            print("=====================================")

