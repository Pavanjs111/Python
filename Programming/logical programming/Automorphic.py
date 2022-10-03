# n=int(input())
# temp=n
# found=False
# t=10
# sq=n*n
# while n>0:
#     rem=sq%t
#     if temp==rem:
#         found=True
#         break
#     t*=10
#     n=n//10
# if found:
#     print("Automorphic")
# else:
#     print("not automorphic")

n=int(input())
c=len(str(n))
sq=n*n
r=str(sq)
r1=r[-1:-(c+1):-1]
I=int(r1[::-1])
if I==n:
    print("Automorphic")
else:
    print("Not Automorphic ")