# n1=int(input())
# n2=int(input())
# min=0
# HCF=1
# if n1==n2:
#     print("both the number are same")
# elif n1<n2:
#     min=n1
# else:
#     min=n2
# # print(f"minimum={min}")
# for i in range(1,min+1):
#     if n1%i==0 and n2%i==0:
#         HCF=i
# print(f"HCF={HCF}")

n1=int(input())
n2=int(input())
s1=set()
s2=set()
for i in range(1,n1+1):
    if n1%i==0:
        s1.add(i)
for i in range(1,n2+1):
    if n2%i==0:
        s2.add(i)
    s3=s1.intersection(s2)
    HCF=max(s3)
print(f"HCF={HCF}")
   

