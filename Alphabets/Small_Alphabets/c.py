def for_c():
    for row in range(6):
        for col in range(4):
            if (row==1 or row==5) and col%3!=0 or (row==2 or row==4)and col%3==0 or col==0 and row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_c():
    row=0
    while row<6:
        col=0
        while col<4:
            if (row==1 or row==5) and col%3!=0 or (row==2 or row==4)and col%3==0 or col==0 and row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
