def for_X():
    """We are creating user defined function for alphabetical pattern of capital X with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i-j==1 or i+j==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_X():
    i=0
    while i<7:
        j=0
        while j<5:
            if i-j==1 or i+j==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()   
