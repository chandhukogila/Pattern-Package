def for_t():
    for row in range(6):
        for col in range(4):
            if row==2 or col==1 and row<5 or row+col==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_t():
    row=0
    while row<6:
        col=0
        while col<4:
            if row==2 or col==1 and row<5 or row+col==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
