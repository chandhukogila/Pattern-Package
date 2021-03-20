def for_minus():
    for row in range(5):
        for col in range(6):
            if row==2 and col>0 and col<5 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_minus():
    row=0
    while row<5:
        col=0
        while col<6:
            if row==2 and col>0 and col<5 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
