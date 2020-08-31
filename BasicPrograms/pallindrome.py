n=int(input("enter a no to check pallindrome or not"))
rev=0
temp=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print(temp," is a pallindrome")
else:
    print(temp,"is not pallindrome")