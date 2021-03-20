def for_S():
    """We are creating user defined function for alphabetical pattern of capital S with "*" symbol"""
    row=7
    col=5
    for i in range(row):
        for j in range(col):
            if ((i==0 or i==3 or i==6)and j%4!=0) or ((i==1 or i==5)and j%4==0)or i==2 and j==0 or i==4 and j==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_S():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((i==0 or i==3 or i==6)and j%4!=0) or ((i==1 or i==5)and j%4==0)or i==2 and j==0 or i==4 and j==4 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()    
