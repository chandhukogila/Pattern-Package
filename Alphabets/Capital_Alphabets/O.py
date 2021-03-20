def for_O():
    """We are creating user defined function for alphabetical pattern of capital O with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i==0 or i==6)and j%4!=0) or ((i==1 or i==5)and j%4==0) or (j==0 or j==4) and i>0 and i<6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_O():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((i==0 or i==6)and j%4!=0) or ((i==1 or i==5)and j%4==0) or (j==0 or j==4) and i>0 and i<6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()  
