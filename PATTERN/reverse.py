# n=int(input())
# s=list(str(n))
# s.reverse()
# c=int("".join(s))
# print(c)

n=int(input())
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)

