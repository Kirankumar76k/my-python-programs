class Square:
    def show(self):
        print("this is show method from b")

class Number:
    def show2(self):
        print("this is show method from a")



class cube(Number,Square):
    def show1(self):
        print("this is show method from cube")



c=cube()
c.show()
