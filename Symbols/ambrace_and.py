def for_ambrace_and():
    for row in range(8):
        for col in range(6):
            if row-col==2 or row+col==9 or row-col==6 or row>0 and (row+col==4) or (col==0 and (row==1 or row==5)) or row==0 and(col>0 and col<3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_ambrace_and():
    row=0
    while row<8:
        col=0
        while col<6:
            if row-col==2 or row+col==9 or row-col==6 or row>0 and (row+col==4) or (col==0 and (row==1 or row==5)) or row==0 and(col>0 and col<3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
