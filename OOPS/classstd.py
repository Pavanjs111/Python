class student:
    c_name="CIT"
    c_pin=560022
    def __init__(self,name,gen,age,num) :
        self.name=name
        self.gen=gen
        self.age=age
        self.num=num

    def fun(self):
        print(f"{self.name} is having fun")

    def run(self):
        print(f"{self.name} is running")
    
    def info(self):
        print(f"name:{ self.name} ")
        print(f"gen:{self.gen}")
        print(f"age:{self.age}")
        print(f"num:{self.num}")
    
student1=student("Pavan","M",22,7406030144)
student2=student("Jishnu","M",22,874056144)
student3=student("Prithvi","M",22,7485630144)

student1.info()
student1.fun()
print(student.c_name)
print(student.c_pin)
print("******************************")
student2.info()
print(student.c_name)
print(student.c_pin)
student2.run()
print("******************************")
student3.info()
student3.fun()
print(student.c_pin)
print(student.c_name)