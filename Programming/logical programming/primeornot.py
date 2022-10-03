# n=int(input())
# c=0
# if n<2:
#     print("cannot find prime number")
# else:
#     for i in range(1,n+1):
#         if n%i==0:
#             c+=1
#     if c==2:
#         print("prime")
#     else:
#         print("not a prime")

n=int(input())
c=0
lc=0
if n<2:
    print("cannot find the prime number")
else:
   for i in range(2,(n//2)+1):
              lc+=1
              print(lc)
              if n%i==0:
                   c+=1
                   break
if c==0:
    print("prime")
else:
    print("not a prime")
    
