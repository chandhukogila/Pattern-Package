def for_upper_cap():
    for row in range(5):
        for col in range(7):
            if row+col==3 or col-row==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_upper_cap():
    row=0
    while row<5:
        col=0
        while col<7:
            if row+col==3 or col-row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
