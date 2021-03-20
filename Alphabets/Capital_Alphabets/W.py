def for_W():
    """We are creating user defined function for alphabetical pattern of capital W with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if j==0 or j==4 or (((i-j==2)or(i+j==6))and i>3) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_W():
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or j==4 or (((i-j==2)or(i+j==6))and i>3) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()   
