#protected are accessible from outside the class but only in a child class
#i.e., derived from it
#Adding a prefix _(single underscore) to a variable name makes it protected


class emp:
    # protected data members
    _id=None
    _name=None
    _phno=None

    def __init__(self,id,name,phno):
        # protected attribute
        self._id=id
        self._name=name
        self._phno=phno

    # protected member function
    def _empdetails(self):
        print("employee id",self._id)
        print("employee name",self._name)

class company(emp):
    def __init__(self,id,name,phno):
        emp.__init__(self,id,name,phno)
    def displaydetails(self):
        self._empdetails()
        print("employee phno",self._phno)



obj=company(1,"somu",99152546625)
obj.displaydetails()
