class car:
    cvar=10
    def __init__(self):
        self.m1=19
        self.com="com"

c1=car()
c2=car()
c1.m1=23
car.cvar=25;
print(c1.m1," ",c2.m1)
print(c1.cvar,"  ",c2.cvar)
print(c2.com)