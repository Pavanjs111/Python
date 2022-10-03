from Has import Employee
class Data:
    def __init__(self,address,salary,emp_obj):
        self.address=address
        self.obj=salary
        self.emp_obj=emp_obj

    def display(self):
        self.emp_obj.empdata()
        print("Address",self.address)
        print("salary",self.salary)

emp=Employee("Pavan",22)
data=Data("Bangalore",2500,emp)
data.display()