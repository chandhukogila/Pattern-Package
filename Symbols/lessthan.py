def for_lessthan():
    for row in range(7):
        for col in range(4):
            if row-col==3 or row+col==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_lessthan():
    row=0
    while row<7:
        col=0
        while col<4:
            if row-col==3 or row+col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
