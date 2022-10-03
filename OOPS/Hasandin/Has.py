# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def empdata(self):
#         print("name of the employee",self.name)
#         print("age of the emploee",self.age)

def fun(n):
    if n>=1 and n<=5:
        return fun(n+1)
    else:
        return fun(n-1)
r=fun(1)
print(r)
