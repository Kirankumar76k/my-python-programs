a=10
b=20
p=2.4
q=5.6

print(a+b)
res1=int.__add__(a,b,q)
res2=float.__add__(p,q)
print(int.__eq__(res1,res2))
print(int.__add__(a,b))
print(float.__add__(p,q))
print(int.__eq__(a,b))
print(int.__sub__(a,b))

