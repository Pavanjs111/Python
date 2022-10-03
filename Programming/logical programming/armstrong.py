n=int(input())
sum=0
temp=n
c=0
while n>0:
    c+=1
    n=n//10
n=temp
while(n>0):
        r=n%10
        sum=sum+r**c
        n=n//10
if sum==temp:
    print("strong")
else:
    print("not strong")

