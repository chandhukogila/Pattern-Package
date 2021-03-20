def for_six():
    """We are creating user defined function for numerical pattern of six with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i==1 or i==4 or i==5)and j%4==0) or ((i==0 or i==6 or i==3) and j%4!=0) or j==0 and i>0 and i<6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_six():
    row=0
    while row<6:
        col=0
        while col<4:
            if (row==5 or row==2 or row==0) and col%3!=0 or (row==3 or row==4 )and col%3==0  or row==2 and col<3 or row==1 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()       
