from turtle import clear


def apf(n, x):
    sum = 1.000
    for i in range(n, 0, -1):
        sum = 1 + x * sum / i
    return(sum)

n = int(input())
x = int(input())
ans=apf(n,x)
print(ans)