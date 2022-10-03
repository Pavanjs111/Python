class one:
    a=100
    def fun(self):
        print("I am fun")
    
    def __init__(self,b,c):
        self.b=b
        self.c=c

o1_one=one(10,20)
o2_one=one(100,200)

print(o1_one.b)
print(o1_one.c)
print(o2_one.b)
print(o2_one.c)
o1_one.fun()
o2_one.fun()