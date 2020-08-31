n=int(input("ënetr any Number"))
rem,rev=0,0

while(n>0):
    temp = n
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10

    if(temp==rev):
        print("palindrome",rev)
        break
    else:
        n=temp+rev


