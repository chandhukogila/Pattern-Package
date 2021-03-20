def for_mul():
    for row in range(5):
        for col in range(7):
            if row==2 or col==3 or row-col==-1 or row+col==5 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_mul():
    row=0
    while row<5:
        col=0
        while col<7:
            if row==2 or col==3 or row-col==-1 or row+col==5 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
