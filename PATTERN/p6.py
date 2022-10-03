n=int(input())
rev=0
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum+r
    n//=10
print("sum is:",sum)
if sum%2==0:
    while temp>0:
        r=temp%10
        rev=rev*10+r
        temp//=10
    print(rev)
else: 
        print("reverse is not possible")

