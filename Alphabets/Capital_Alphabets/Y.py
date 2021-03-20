def for_Y():
    """We are creating user defined function for alphabetical pattern of capital Y with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i-j==0 or i+j==4)and i<3) or j==2 and i>2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_Y():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((i-j==0 or i+j==4)and i<3) or j==2 and i>2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()       
