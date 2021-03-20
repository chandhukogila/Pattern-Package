def for_double_quotes():
    for row in range(4):
        for col in range(4):
            if row+col==1 or row+col==3 and row<2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_double_quotes():
    row=0
    while row<4:
        col=0
        while col<4:
            if row+col==1 or row+col==3 and row<2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
