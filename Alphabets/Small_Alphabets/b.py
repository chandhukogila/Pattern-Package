def for_b():
    for row in range(6):
        for col in range(4):
            if col==0 or row-col==3 or col==3 and (row==3 or row==4) or row==2 and col<3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_b():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==0 or row-col==3 or col==3 and (row==3 or row==4) or row==2 and col<3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()  
