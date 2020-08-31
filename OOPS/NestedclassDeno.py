class Student:
    def __init__(self,rollno,age):
        self.rolno=rollno
        self.age=age
        self.lap=Laptop()

    def show(self):
        print(self.rolno,self.age)
        self.lap.show()
class Laptop:
    def __init__(self):
        self.ram="4gb"
        self.rom = "1tb"

    def show(self):
        print(self.ram,self.rom)


s1=Student(12,20)
s2=Student(13,78)
s1.show()
s2.show()