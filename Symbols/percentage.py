def for_percentage():
    for row in range(5):
        for col in range(5):
            if row+col==4 or (row==0 or row==1)and (col<2)or (row==3 or row==4)and col>2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_percentage():
    row=0
    while row<5:
        col=0
        while col<5:
            if row+col==4 or (row==0 or row==1)and (col<2)or (row==3 or row==4)and col>2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
