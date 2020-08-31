class A:
    def show(self):
        print("show in A")

class B(A):
    pass
    def show(self):
       super().show()
       print("show in B")


s=B()
s.show()