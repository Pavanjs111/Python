n=int(input())
sum=0
for i in range(1,(n//2+1)):
    if n%1==0:
        sum+=i

if sum==n:
    print("perfect")
else:
    print("not a perfect")