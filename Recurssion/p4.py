def fun(num):
    if num>1:
        fun(num//2)
    print(num%2,end="")
num=int(input("Enter the number"))
fun(num)