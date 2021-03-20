def for_I():
    """We are creating user defined function for alphabetical pattern of capital   with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i==0 or i==6)and j>0 and j<4) or j==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_I():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((i==0 or i==6)and j>0 and j<4) or j==2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()   
