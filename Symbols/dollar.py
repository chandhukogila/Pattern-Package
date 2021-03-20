def for_dollar():
    for row in range(9):
        for col in range(5):
            if (row==1 or row==7) and (col>0 and col<4) or row-col==2 or col==2 or (row==2 or row==6) and (col==0 or col==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_dollar():
    row=0
    while row<9:
        col=0
        while col<5:
            if (row==1 or row==7) and (col>0 and col<4) or row-col==2 or col==2 or (row==2 or row==6) and (col==0 or col==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
