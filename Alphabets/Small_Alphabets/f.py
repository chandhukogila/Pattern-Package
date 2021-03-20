def for_f():
    for row in range(6):
        for col in range(4):
            if col==1 or row==2 and col<3 or row==0 and col==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_f():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==1 or row==2 and col<3 or row==0 and col==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()     
