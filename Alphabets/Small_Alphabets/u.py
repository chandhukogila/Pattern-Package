def for_u():
    for row in range(5):
        for col in range(4):
            if row-col==3 or (col==0 or col==2) and row<4 or row==4 and col==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_u():
    row=0
    while row<5:
        col=0
        while col<4:
            if row-col==3 or (col==0 or col==2) and row<4 or row==4 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
