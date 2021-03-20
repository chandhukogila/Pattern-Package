def for_seven():
    """We are creating user defined function for numerical pattern of seven with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==0 or i==1 and j%4==0 or i+j==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_seven():
    row=0
    while row<6:
        col=0
        while col<4:
            if row==0  or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()  
