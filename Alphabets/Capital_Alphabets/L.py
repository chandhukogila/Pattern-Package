def for_L():
    """We are creating user defined function for alphabetical pattern of capital L with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==6 or j==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_L():
    i=0
    while i<7:
        j=0
        while j<5:
            if i==6 or j==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()  
