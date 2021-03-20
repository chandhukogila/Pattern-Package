def for_semi_collon():
    for row in range(4):
        for col in range(4):
            if (row==0 or row==2) and col==1 or col==0 and row>2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_semi_collon():
    row=0
    while row<4:
        col=0
        while col<6:
            if (row==0 or row==2) and col==1 or col==0 and row>2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
