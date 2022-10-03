n=int(input())
temp=n
c=len(str(n-1))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**c
    c-=1
    n=n//10
if sum==temp:
    print("Disaurim")
else:
    print("not disaurim")