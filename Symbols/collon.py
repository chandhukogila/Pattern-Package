def for_collon():
    for row in range(4):
        for col in range(4):
            if (row==1 or row==3) and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_collon():
    row=0
    while row<4:
        col=0
        while col<4:
            if (row==1 or row==3) and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
