def for_exclamatory():
    for row in range(7):
        for col in range(4):
            if row<4 and (col==1 or col==2)or row>4 and (col==1 or col==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_exclamatory():
    row=0
    while row<7:
        col=0
        while col<4:
            if row<4 and (col==1 or col==2)or row>4 and (col==1 or col==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
