n=int(input())
temp=n**2
sum=0
num=n
while temp>0:
    rem=temp%10

    sum=sum+rem
    temp=temp//10
if sum==num:
    print("Neon number")
else:
    print("not a neon number")