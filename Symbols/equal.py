def for_equal():
    for row in range(4):
        for col in range(6):
            if (row==1 or row==3)and (col>0 and col<5) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_equal():
    row=0
    while row<4:
        col=0
        while col<6:
            if (row==1 or row==3)and (col>0 and col<5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
