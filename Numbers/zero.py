def for_zero():
    """We are creating user defined function for numerical pattern of zero with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i==0  or i==6)and j%4!=0) or ((i==1 or i==2 or i==4 or i==5 or i==3)and j%4==0) or i+j==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_zero():
    row=0
    while row<6:
        col=0
        while col<4:
            if (col==0 or col==3) and (row>0 and row<5) or (row==0 or row==5) and col%3!=0 or row+col==4 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()        
        
