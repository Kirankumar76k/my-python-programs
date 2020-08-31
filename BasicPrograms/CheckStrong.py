#strong number is a number that is sum of factorials is equals to original no
n = int(input("enter no to check strong number or not"))
temp=n
sum=0
while(n>0):
    rem=n%10
    i=1
    res=1
    while(i<=rem):
        res=res*i
        i+=1
    sum=sum+res
    n=n//10
if(temp==sum):
    print(temp, "is a strong number")
else:
    print(temp, "is not strong number")
