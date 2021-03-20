def for_four():
    """We are creating user defined function for numerical pattern of four with "*" symbol """
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i+j==4 or i==4 or j==4 and i>2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_four():
    row=0
    while row<6:
        col=0
        while col<4:
            if row+col==2 or row==3 or (col==2 and row>0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print() 
