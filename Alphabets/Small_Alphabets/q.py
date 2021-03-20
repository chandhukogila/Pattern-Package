def for_q():
    for row in range(6):
        for col in range(4):
            if col==3  or row==3 and col>0 or col-row==1 or col==0 and(row>0 and row<3) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_q():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==3  or row==3 and col>0 or col-row==1 or col==0 and(row>0 and row<3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()  
