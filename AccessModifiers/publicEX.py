#public are accessible from outside the class through an object of the class
class employee:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

class dept:
    def show(self):
        print("dummy class")

obj = employee("kiran", 25)
print(obj.age)
print(obj.name)