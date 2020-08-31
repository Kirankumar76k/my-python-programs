# Access File
import Functions
if _name=='main_':
    checkprime=[]
    prime=[]
    n=int(input("enter ur range"))
    for i in range(n):
        checkprime.append(int(input()))
    for i in checkprime:
        if(Functions.checkPrime(i)):
            prime.append(i)

    print(prime)

    checkfib = []
    fib = []
    n = int(input("enter ur range"))
    for i in range(n):
        checkfib.append(int(input()))
    for i in checkfib:
        if (Functions.checkFib(i)):
            fib.append(i)

    print(fib)

    checkstrong = []
    strong = []
    s=int(input("enter first range"))
    n = int(input("enter last range"))
    # for i in range(n):
    #     checkstrong.append(int(input()))
    for i in range(s,n):
        if (Functions.checkStrong(i)):
            strong.append(i)

    print(strong)

    # some more functions need to be implemented...but  i ignore