class A:
    def __init__(self):
        print("this is from A class")


class B(A):
    def __init__(self):
        super().__init__()
        print("this is from B class")

b=B()