def for_F():
    """We are creating user defined function for alphabetical pattern of capital F with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if j==0 or i==0 or i==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_F():
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or i==0 or i==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()        
