def for_hash():
    for row in range(5):
        for col in range(9):
            if row+col==4 or row+col==7 or (row==1 and col>0)or (row==3) and col<7  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_hash():
    row=0
    while row<5:
        col=0
        while col<9:
            if row+col==4 or row+col==7 or (row==1 and col>0)or (row==3) and col<7 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
