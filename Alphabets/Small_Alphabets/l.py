def for_l():
    for row in range(6):
        for col in range(4):
            if col==1  and row<5or (row==5 and (col==0 or col==2 or col==3))  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_l():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==1  and row<5or (row==5 and (col==0 or col==2 or col==3)) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()     
