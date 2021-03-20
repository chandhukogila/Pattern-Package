def for_fullstop():
    for row in range(5):
        for col in range(4):
            if row==3 and col==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_fullstop():
    row=0
    while row<4:
        col=0
        while col<6:
            if  row==3 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
