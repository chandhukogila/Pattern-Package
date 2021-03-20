def for_H():
    """We are creating user defined function for alphabetical pattern of capital H with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==3 or j==0 or j==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_H():
    i=0
    while i<7:
        j=0
        while j<5:
            if i==3 or j==0 or j==4 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()        
