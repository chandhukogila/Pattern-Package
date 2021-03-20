def for_hyphen():
    for row in range(3):
        for col in range(3):
            if row==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_hyphen():
    row=0
    while row<3:
        col=0
        while col<3:
            if row==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
