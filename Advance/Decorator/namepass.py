def outer_fun(num):
    def inner_fun1():
        print("Hi I am Jack")

    def inner_fun2():
        print("hello I am rose")

    if num==1:
        return inner_fun1()
    return inner_fun2()

outer_fun(1)
print()
outer_fun(10)