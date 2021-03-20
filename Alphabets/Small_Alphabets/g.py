def for_g():
    for row in range(6):
        for col in range(3):
            if row-col==2 or col-row==1 or row+col==4 or col==2 and row>0 or row==5 and col==1 or row==1 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_g():
    row=0
    while row<6:
        col=0
        while col<3:
            if row-col==2 or col-row==1 or row+col==4 or col==2 and row>0 or row==5 and col==1 or row==1 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()  
