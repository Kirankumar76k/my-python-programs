class employee:
    salary=10000
    def __init__(self,empid,dept):
        self.empid=empid
        self.dept=dept
    def display(self):
        print(self.empid,self.dept,self.salary)

kiran=employee(1,"hr")
somu=employee(2,"IT")
bangar=employee(3,"pp")

kiran.display()
somu.display()
bangar.display()
employee.salary=12000
print("after incrementing salary")
kiran.display()
somu.display()
bangar.display()