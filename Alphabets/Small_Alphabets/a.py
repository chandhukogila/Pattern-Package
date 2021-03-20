def for_a():
    for row in range(6):
        for col in range(4):
            if (col==0 or col==2) and row%5!=0 or col==1 and (row==0 or row==5) or row+col==8:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_a():
    row=0
    while row<6:
        col=0
        while col<4:
            if (col==0 or col==2) and row%5!=0 or col==1 and (row==0 or row==5) or row+col==8:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
