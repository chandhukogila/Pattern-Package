def for_attherate():
    for row in range(8):
        for col in range(9):
            if row+col==2 or row-col==5 or col-row==6 or (row==0 or row==7) and (col<6 and col>1) or (row==3 or row==4)and (col==0 or col==8 or col==3 or col==6) or (row==2 or row==5)and(col==4 or col==5) or (row==5)and (col==6 or col==8) or row==6 and col==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_attherate():
    row=0
    while row<8:
        col=0
        while col<9:
            if row+col==2 or row-col==5 or col-row==6 or (row==0 or row==7) and (col<6 and col>1) or (row==3 or row==4)and (col==0 or col==8 or col==3 or col==6) or (row==2 or row==5)and(col==4 or col==5) or (row==5)and (col==6 or col==8) or row==6 and col==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()        
