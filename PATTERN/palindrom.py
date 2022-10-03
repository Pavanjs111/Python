
# n=int(input())
# temp=n
# s=list(str(n))
# s.reverse()
# c=int("".join(s))
# if temp==c:
#     print("palindrome")
# else:
#     print("not a palindrome")


n=int(input())
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")