#a series of a numbers in which no is the sum of two presceding numbers.
n=int(input("enter a no to print upto fibonnacci series"))
a,b=0,1
i=0
while(i<n):
   print(a)
   #a,b=b,a+b
   c=a+b
   a=b
   b=c
   i += 1

#fibbonacci with generators
# def fib():
#     f,s=0,1
#     while True:
#         yield f
#         f,s=s,f+s
# for x in fib():
#     if x>50:
#         break;
#     print(x,end=" ")
