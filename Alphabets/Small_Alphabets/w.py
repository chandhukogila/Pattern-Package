def for_w():
    for row in range(5):
        for col in range(5):
            if (row<4 and row>0)and col%2==0 or (row==4 and col%2!=0) or row==0 and col%4==0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_w():
    row=0
    while row<5:
        col=0
        while col<5:
            if (row<4 and row>0)and col%2==0 or (row==4 and col%2!=0) or row==0 and col%4==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
