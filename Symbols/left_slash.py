def for_left_slash():
    for row in range(5):
        for col in range(5):
            if row-col==0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_left_slash():
    row=0
    while row<5:
        col=0
        while col<5:
            if row-col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
