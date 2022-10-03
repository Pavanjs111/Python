n1=int(input())
n2=int(input())
if n1>n2:
    max=n1
else:
    max=n2
while True:
    if max%n1==0 and max%n2==0:
        LCM=max
        break
    max+=1
print(f"LCM is {LCM}")

# n1=int(input())
# n2=int(input())
# LCM=0
# lc=0
# max=max(n1,n2)
# t=max
# while True:
#     lc+=1
#     if max%n1==0 and max%n2==0:
#         LCM = max
#         break
#     max+=t
# print(f"The lcm of {n1} and {n2} is {LCM}")
# print(lc)
