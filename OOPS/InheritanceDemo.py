#multi level inheritance

class parent:
    def land(self):
        print("Suvarna bhoomi land")
    def gold(self):
        print("vaddanam mariyu vendi molathadu")
class child(parent):
    def ricemill(self):
        print("rice mill")
class grandchild(child):
    def gold(self):
        super().gold()
        print("Bangaru siggu billa")

obj=grandchild()
obj.land()
obj.gold()

