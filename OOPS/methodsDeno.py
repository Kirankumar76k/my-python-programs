class Student:
    college="Miracle"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1+self.m2+self.m3)//3

    @classmethod
    def info(cls):
        print(cls.college)

    @staticmethod
    def infoclass():
        print("this is belongs to differnt types of methods")



somnadh = Student(94,97,58)
kiran = Student(19,49,33)

print(somnadh.avg())
print(kiran.avg())
Student.info()
somnadh.info()
kiran.info()
Student.infoclass()

