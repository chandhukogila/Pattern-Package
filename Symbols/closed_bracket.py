def for_closed_bracket():
    for row in range(5):
        for col in range(5):
            if col==3 or col==2 and(row==0 or row==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_closed_bracket():
    row=0
    while row<5:
        col=0
        while col<5:
            if col==3 or col==2 and(row==0 or row==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
