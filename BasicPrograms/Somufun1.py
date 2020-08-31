# Fuction file
def checkPrime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
            break
    if(c==0):
        return True
    else:
        return False


def checkFib(n):
        a=0
        b=1
        c=1
        flag=0
        if((n==1) or (n==0)):
            return True
        else:
            while(n>c):
                c=a+b
                if(n==c):
                    flag=1
                    break
                a=b
                b=c

            if(flag==1):
                return True
            else:
                return False


def checkStrong(n):
    sum = 0
    temp=n
    while(n>0):
        f=n%10
        fact=1
        for i in range(1,f+1):
            fact=fact*i
        sum=fact+sum
        n=n//10
    if(temp==sum):
        return True
    else:
        return False



def checkPerfect(n):
    sum=0
    temp=n
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(temp==sum):
        return True
    else:
        return False


def checkArmStrong(n):
    sum = 0
    temp = n
    while (n > 0):
        f = n % 10
        cube=f*f*f

        sum = cube + sum
        n = n // 10
    if (temp == sum):
        return True
    else:
        return False


def checkStringPalindrome(n):
    rev=n[::-1]
    if n==rev:
        return True
    else:
        return False



def checkNumPalindrome(n):
    temp = n
    rev=0
    while (n > 0):
        rem = n % 10
        rev=rev*10+rem
        n = n // 10
    if (temp == rev):
        return True
    else:
        return False

# ========================================================================================================================
# print(checkPrime(5))
# print(checkFib(3))
# print(checkStrong(145))
# print(checkPerfect(28))
# print(checkArmStrong(153))
# print(checkStringPalindrome("malayalam"))
# print(checkNumPalindrome(121)