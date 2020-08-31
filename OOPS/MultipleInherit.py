class Husband:
    def watch(self):
        print("Titan 100 rupai watch")

class wife:
    def watch1(self):
        print("paaki watch")

class son(wife,Husband):
    def watch(self):
        print("dhobbukochina watch")

obj=son()
obj.watch()