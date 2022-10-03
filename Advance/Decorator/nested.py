def fun_outer():
    print("outer fun started")
    def inner_fun1():
        print("I am jack")

    def inner_fun2():
        print("hello i am rose")

    inner_fun1()
    inner_fun2()


fun_outer()
print("outerfun ended")