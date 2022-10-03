class one:
    a=100
    def __init__(self,b):
        self.b=b

    def fun(self):
        print("I am fun")

        # Accessing public members within the module and outside the class
one_1=one(10)
print(one_1.b)
print(one_1.a)
one_1.fun()
