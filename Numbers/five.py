def for_five():
    """We are creating user defined function with numerical pattern of five with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==0 or j==0 and i<4 or ((i==3 or i==6) and j%4!=0) or j==4 and (i>3 and i<6) or i==5 and j==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_five():
    row=0
    while row<6:
        col=0
        while col<4:
            if row==0 or col==0 and (row<3 or row==4) or row==2 and col<3 or col==3 and (row==3 or row==4) or row==5 and col%3!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()   
