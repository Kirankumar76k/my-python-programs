class demo:
    def addition(self,*args):
        add=0
        for i in args:
            add=add+i
        return add
d=demo()
print(d.addition(18,15))
#print(d.addition("kiran","ssss"))
print(d.addition(2.8,1))
print(d.addition(12,1,98,8888888,5))