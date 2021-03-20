def for_h():
    for row in range(6):
        for col in range(4):
            if col==0 or col==3 and row>1 or row==1 and col==2 or col==1 and row==2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_h():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==0 or col==3 and row>1 or row==1 and col==2 or col==1 and row==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()        
