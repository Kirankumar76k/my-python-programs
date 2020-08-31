#private are accessible only within the class
#data members of  a class are declared private by adding a double under score
#before the data member of a class
class student:
    #private data members
    __name=None
    __age=None
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    #private member function
    def __displaydetails(self):
        print("name of student",self.__name)
        print("age of student",self.__age)

    #public member function
    def accessPrivateFunction(self):
        #Accessing private member function
        self.__displaydetails()
obj=student("kiran",25)
obj.displaydetails()
obj.accessPrivateFunction()