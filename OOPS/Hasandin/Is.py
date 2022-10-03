class Apple:
    def __init__(self):
        print("class a constructor")

    def m1(self):
        print("M1 method of class a")

class Ball:
    def __init__(self):
        print("class B constructor")

    def m2(self):
        obj=Apple()

        obj.m1()  

obj=Ball()
obj.m2()