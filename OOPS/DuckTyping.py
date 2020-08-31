class PyeCharm:

    def excute(self):
        print("compiling")
        print("Running")



class MyEditor:

    def excute(self):
        print("SpellCheck")
        print("ConventionCheck")
        print("compiling")
        print("Running")




class Laptop:

    def code(self,ide):
        ide.excute()


ide=MyEditor()
#ide=PyeCharm()
lap1=Laptop()
lap1.code(ide)