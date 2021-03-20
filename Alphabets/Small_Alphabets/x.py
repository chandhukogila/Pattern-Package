def for_x():
    for row in range(5):
        for col in range(4):
            if row-col==1 or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_x():
    row=0
    while row<5:
        col=0
        while col<4:
            if row-col==1 or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print() 
