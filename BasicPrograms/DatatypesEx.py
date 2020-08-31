list1=["kiran",3,'kumar',32,4j,"hellooo"]
print(list1)
print(list1[2])
print(list1[2:5])
print(list1[-5:-2])
print(list1[:4])
print(list1[3])
print(list1[3:])
list1.append("append object")
list1.insert(3,"4th postion")
list1.remove('kumar')
#print all items in the list one by one
for x in list1:
    print(x)
print(len(list1))