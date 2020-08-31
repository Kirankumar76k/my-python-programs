class Demo:
    def addition(self,*args):
        s=0;
        for i in args:
            s=s+i


d=Demo()
print(d.addition(6,7,8))
print(d.addition(8.5,7,8))