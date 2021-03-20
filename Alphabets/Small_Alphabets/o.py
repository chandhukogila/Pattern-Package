def for_o():
    for row in range(5):
        for col in range(4):
            if (row==0 or row==4) and col%3!=0 or (row==1 or row==2 or row==3) and col%3==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_o():
    row=0
    while row<5:
        col=0
        while col<4:
            if (row==0 or row==4) and col%3!=0 or (row==1 or row==2 or row==3) and col%3==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()        
