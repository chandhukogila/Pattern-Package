def for_two():
    """We are creating user defined function for numerical pattern of two with "*" symbol """
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==0 and j%4!=0 or i==1 and j%4==0 or i+j==6 or i==6 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_two():
    row=0
    while row<6:
        col=0
        while col<4:
            if row==0 and col%3!=0 or row==1 and col%3==0 or row+col==5  or row==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()     
