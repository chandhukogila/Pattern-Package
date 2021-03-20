def for_comma():
    for row in range(5):
        for col in range(4):
            if row+col==6 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_comma():
    row=0
    while row<5:
        col=0
        while col<4:
            if row+col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
