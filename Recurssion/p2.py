def fun(n):
    if n<5:
        print(n,end="")
        fun(n+1)
    print(n, end="")
fun(1)