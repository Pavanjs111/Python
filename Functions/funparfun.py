def fun(x,y):
    print("start of the fun")
    x()
    print("end of fun")
    print("start of the fun")
    y()
    print("end of fun")
    
    

def fun2():
    print("start of fun2")
    print("this is fun2")
    print("end of fun2")

def fun3():
    print("start of fun3")
    print("this is fun3")
    print("end of fun3")

print("start")
fun(fun2,fun3)
print("end")
