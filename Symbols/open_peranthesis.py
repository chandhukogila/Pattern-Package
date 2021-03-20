def for_open_peranthesis():
    for row in range(7):
        for col in range(4):
            if  row-col==4 or row+col==2 or col==0 and row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_open_peranthesis():
    row=0
    while row<7:
        col=0
        while col<4:
            if row-col==4 or row+col==2 or col==0 and row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
