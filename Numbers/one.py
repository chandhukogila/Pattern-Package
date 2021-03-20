def for_one():
    """
    We are creating a user defined function for numerical pattern of One with "*" symbol
    """
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if i==1 and j<3 or j==2 or i==6 and j<5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_one():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==2 or row==5  or row==1 and col<3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1         
        print()    
