def for_s():
    for row in range(6):
        for col in range(3):
            if (row==0 or row==2 or row==5) and col%2!=0 or (row==1 or row==4) and col%2==0 or row-col==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_s():
    row=0
    while row<6:
        col=0
        while col<3:
            if (row==0 or row==2 or row==5) and col%2!=0 or (row==1 or row==4) and col%2==0 or row-col==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()   
