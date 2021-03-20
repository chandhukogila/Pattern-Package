def for_or():
    for row in range(5):
        for col in range(5):
            if col==2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_or():
    row=0
    while row<5:
        col=0
        while col<5:
            if col==2 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
