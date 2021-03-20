def for_down_cap():
    for row in range(5):
        for col in range(7):
            if row-col==1 or row+col==7 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_down_cap():
    row=0
    while row<5:
        col=0
        while col<7:
            if row-col==1 or row+col==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
