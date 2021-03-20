def for_xor():
    for row in range(4):
        for col in range(6):
            if row==1 and(col==1 or col==2 or col==5) or row==2 and (col==0 or col==3 or col==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_xor():
    row=0
    while row<4:
        col=0
        while col<6:
            if row==1 and(col==1 or col==2 or col==5) or row==2 and (col==0 or col==3 or col==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
