#sum of positive divisors excluding the no itself is equal to that no
n=int(input("enter a no to check perfect number or not"))
i=1
res=0
while(i<n):
    if(n%i==0):
        res=res+i
    i+=1
if(res==n):
    print("perfect")
else:
    print("not perfect")