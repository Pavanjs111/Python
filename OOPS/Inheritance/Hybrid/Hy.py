class school:
    def fun1(self):
        print("I am the school")
    
class teacher1(school):
    def fun2(self):
        print("I am teacher1")
    
class teacher2(school):
    def fun3(Self):
        print("Teacher2 from school")
    
class student(teacher1,teacher2):
    def fun4(self):
        print("I am student")

obj=student()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()