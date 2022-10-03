
def fun():
    def inner_fun():
        print("how are you doing today")
    
    def inner_fun2():
        print("how are everyone chilling")
    return inner_fun(),inner_fun2()

a,b=fun()
a()
b()