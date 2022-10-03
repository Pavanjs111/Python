def fun1():
    print("running fun 1")
    x=10
    def fun2():
        print("running fun 2")
        print(x)
    return fun2

a=fun1()
print(a.__name__)
a()