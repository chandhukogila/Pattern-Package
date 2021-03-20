def for_question_mark():
    for row in range(7):
        for col in range(4):
            if (col==0 or col==3) and (row==1) or col==1 and (row==0 or row==3 or row==4 or row==6)or col==2 and (row==0 or row==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_question_mark():
    row=0
    while row<7:
        col=0
        while col<4:
            if (col==0 or col==3) and (row==1) or col==1 and (row==0 or row==3 or row==4 or row==6)or col==2 and (row==0 or row==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
