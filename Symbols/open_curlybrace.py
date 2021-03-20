def for_open_curlybrace():
    for row in range(7):
        for col in range(3):
            if col==1 and (row!=3 and row!=0 and row!=6) or col==0 and row==3  or col==2 and (row==0 or row==6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_open_curlybrace():
    row=0
    while row<7:
        col=0
        while col<3:
            if col==1 and (row!=3 and row!=0 and row!=6) or col==0 and row==3  or col==2 and (row==0 or row==6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
