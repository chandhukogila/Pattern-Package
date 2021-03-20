def for_y():
    for row in range(5):
        for col in range(4):
            if row+col==4 or row-col==0 and col<3 or row==0 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_y():
    row=0
    while row<5:
        col=0
        while col<4:
            if row+col==4 or row-col==0 and col<3 or row==0 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
