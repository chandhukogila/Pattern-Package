def for_z():
    for row in range(5):
        for col in range(4):
            if row==1 or row==4 or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_z():
    row=0
    while row<5:
        col=0
        while col<4:
            if row==1 or row==4 or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
