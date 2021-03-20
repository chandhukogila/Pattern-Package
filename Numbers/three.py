def for_three():
    """We are creating user defined function for numerical pattern of three with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i==0 or i==3 or i==6) and j%4!=0) or (i==1 or i==5) and j%4==0 or (i==2 or i==4) and j>3  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_three():
    row=0
    while row<6:
        col=0
        while col<4:
            if row==0 or (row==2 or row==5) and col%3!=0 or row==4 and col%3==0 or col==2 and (row==1) or col==3 and row==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()     
