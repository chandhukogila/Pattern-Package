def for_A():
    """We are creating user defined function for alphabetical pattern of capital A with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((j==0 or j==4)and i>0)or ((i==0 or i==4)and j>0 and j<4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_A():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((j==0 or j==4)and i>0)or ((i==0 or i==4)and j>0 and j<4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()        
