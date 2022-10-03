n=int(input())
cz=0
co=0
ce=0
while n>0:
    n1=n%10
    if n1%2==0:
        ce=0
    elif n1%2!=0:
            co+=1
    else:
        cz+=1
n=n//10
print(ce)
print(co)
print(cz)
