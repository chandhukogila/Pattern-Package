def for_P():
    """We are creating user defined function for alphabetical pattern of capital P with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if j==0 or (i==0 or i==3) and j<4 or j==4 and i>0 and i<3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_P():
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or (i==0 or i==3) and j<4 or j==4 and i>0 and i<3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()      
