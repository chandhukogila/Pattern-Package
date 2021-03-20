def for_n():
    for row in range(5):
        for col in range(4):
            if row==0 and col%2==0 or (col==1 or col==3) and row>0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_n():
    row=0
    while row<6:
        col=0
        while col<4:
            if row==0 and col%2==0 or (col==1 or col==3) and row>0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
