#id is same when the variables(int,string etc.,) values are same where as
#id of object is different even the values are same
#we are accessing class variables through the classname.variable name



class Test:
  a,b,c=10,2,3
  def Add(self,p,q,z):
    return p+q+z

v=1000
k=1000
obj=Test()
obj1=Test()
s=obj.Add(10,20,30)
m=obj1.Add(10,20,30)
print(s)
print(m)
print(Test.a,Test.b,Test.c)
print('\n')
print(id(s))#variable id
print(id(m))#variable id
print('\n')
print(id(obj))#object id
print(id(obj1))#object id
print('\n')
print(id(v))#variable id
print(id(k))#variable id
print('/n')
print(type(v))# this variable differs integer type
print(type(obj))# where this object type is belongs to Main class
