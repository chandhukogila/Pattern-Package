def for_m():
    for row in range(6):
        for col in range(6):
            if row==0 and col%2==0 or (col==1 or col==3 or col==5)and row>0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_m():
    row=0
    while row<6:
        col=0
        while col<6:
            if row==0 and col%2==0 or (col==1 or col==3 or col==5)and row>0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print() 
