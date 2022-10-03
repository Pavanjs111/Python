# n=int(input())
# sum=0
# temp=n
# while n>0:
#     rem = n%10
#     fact=1
#     for i in range(1,rem+1):
#         fact = fact*i
#     sum=sum+fact
#     n=n//10   
# if sum==temp:
#     print("strong")
# else:
#     print("not strong")


n=int(input())
sum=0
temp=n
while n>0:
    rem=n%10
    fact=1
    i=1
    while(i<=rem):
        fact=i*fact
        i+=1

    sum+=fact
    n=n//10
if sum==temp:
    print("strong")
else:
    print("not strong")