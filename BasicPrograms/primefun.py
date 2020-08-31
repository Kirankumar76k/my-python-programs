
def prime(n):
    for i in range(1, n+1):
        if(n%i==0):
            count=+1
    if(count==2):
        print("prime")
        return 1
    else:
        print("composite")
        return 0
count=0
n=int(input("enter a no to check prime or not"))
prime(n)
