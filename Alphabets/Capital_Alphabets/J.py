def for_J():
    """We are creating user defined function for alphabetical pattern of capital J with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==0 or (j==2 and i<6)or i-j==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_J():
    i=0
    while i<7:
        j=0
        while j<5:
            if i==0 or (j==2 and i<6)or i-j==5 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()  
