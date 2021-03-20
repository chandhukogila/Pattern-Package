def for_i():
    for row in range(6):
        for col in range(4):
            if col==1 and row!=1 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_i():
    row=0
    while row<6:
        col=0
        while col<4:
            if col==1 and row!=1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()  
