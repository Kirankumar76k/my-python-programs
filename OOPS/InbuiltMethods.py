a=10
b=20
c=10.4
d=6.7
e=10
res1=int.__add__(a,b)
res2=float.__add__(c,d)
print(res1,res2)
print(int.__eq__(res1,res2))
print(int.__sub__(a,b))
print(int.__eq__(a,e))
print((int.__eq__(a,b)))