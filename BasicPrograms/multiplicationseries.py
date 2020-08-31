n=int(input("enter a no upto print a multiplication tables"))
for i in range(2,n+1):
    for j in range(1,13):
        print(i,"x",j,"=",i*j)
    print("------------")