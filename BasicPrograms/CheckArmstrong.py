#armstrong number is a number that is equals to sum of cubes of its if digits.:
#eg:0,1,153,370,371,407
n=int(input("enter no to check armstrong or not"))
temp=n
res=0
while(n>0):
    rem=n%10;
    res=res+(rem**3)
    n=n//10
if(res==temp):
    print(temp," is a armstrong number")
else:
    print(temp,"is not an armstrong number")
