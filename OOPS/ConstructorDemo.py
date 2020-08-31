class student:
    college="miracle"
    def __init__(self,name,no,age):
        self.name=name
        self.no=no
        self.age=age
    def show(self):
        print("your name=",self.name)
        print("your no=",self.no)
        print("your age=",self.age)

    def add(self):
        print("hai this main clasas")

if __name__ == '__main__':
    s=student("love",2,23)
    s1=student("jjjj",9,80)

    s1.show()


