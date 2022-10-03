def fun(*arg):
    print(arg)
    print(type(arg))
    sum=0
    for i in arg:
        sum=sum+i
        print(sum)


fun()
fun(10)
fun(10,20,30,40,50)
