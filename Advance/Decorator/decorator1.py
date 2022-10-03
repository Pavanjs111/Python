def mydecorator(fun):
    def inner_fun1():
        print("before fun call")
        fun()
        print("after fun call")
    return inner_fun1


def myfunction():
    print("this is my function")

val=mydecorator(myfunction)
val()
