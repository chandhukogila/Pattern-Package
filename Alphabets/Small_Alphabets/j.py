def for_j():
    for row in range(6):
        for col in range(4):
            if col==2 and (row!=1 and row!=5) or row-col==4 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_j():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==2 and (row!=1 and row!=5) or row-col==4 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()  
