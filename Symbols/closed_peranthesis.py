def for_closed_peranthesis():
    for row in range(7):
        for col in range(4):
            if row-col==-1 or row+col==7  or row==3 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_closed_peranthesis():
    row=0
    while row<7:
        col=0
        while col<4:
            if row-col==-1 or row+col==7  or row==3 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
