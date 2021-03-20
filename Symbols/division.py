def for_division():
    for row in range(7):
        for col in range(6):
            if (row==0 or row==1 or row==5 or row==6) and (col==2 or col==3) or row==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_division():
    row=0
    while row<7:
        col=0
        while col<6:
            if (row==0 or row==1 or row==5 or row==6) and (col==2 or col==3) or row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
