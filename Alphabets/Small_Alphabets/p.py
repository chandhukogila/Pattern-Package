def for_p():
    for row in range(6):
        for col in range(4):
            if col==0 or row==3 and col<3 or (row==1 or row==2) and col%3==0 or col+row==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_p():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==0 or row==3 and col<3 or (row==1 or row==2) and col%3==0 or col+row==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print() 
