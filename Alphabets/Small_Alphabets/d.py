def for_d():
    for row in range(6):
        for col in range(4):
            if col==3 or row+col==6 or row-col==4 or row==2 and col>0 or row==3 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_d():
    row=0
    while row<6:
        col=0
        while col<4:
            if  col==3 or row+col==6 or row-col==4 or row==2 and col>0 or row==3 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()     
