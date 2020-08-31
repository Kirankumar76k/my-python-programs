class computer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self):
        print("hai this is constructor")

    def show(self):
        print("ur name:",self.name )
        print("ur age:", self.age)

    def update(self):
        self.age = 25

    def addition(self, som, ish):
        print("addition of two ages are:", (som + ish))

    def compare(self, other):
        if (self.age == other.age):
            return True
        else:
            return False


c1 = computer('somu',12)
c2 = computer('janu',77)

c1.show()
c2.show()

print(id(c1))
print(id(c2))
print(type(c1))
print(type(a))
if(c1.compare(c2)):
    print("same age and same name")
else:
    print("Different age and different name")
c2.name="Ishitha"
c2.update()

print("somnadh age=",c1.age)
print("ishitha age=",c2.age)
c1.addition(c1.age,c2.age)
if(c1.compare(c2)):
    print("same age and same name")
else:
    print("Different age and different name")
print(id(c1))
print(id(c2))

