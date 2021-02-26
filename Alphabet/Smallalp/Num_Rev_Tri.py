num=int(input("enter rows"))
for i in range(num,0,-1):
    for j in range(1,num-i+1):
        print(end=" ")
    
    for j in range(i,1,-1):
        print(j,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
