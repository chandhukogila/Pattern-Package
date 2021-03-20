def for_greaterthan():
    for row in range(7):
        for col in range(4):
            if col-row==0 or row+col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_greaterthan():
    row=0
    while row<7:
        col=0
        while col<4:
            if col-row==0 or row+col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
