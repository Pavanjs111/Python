l1=[1,2,3,4,5]
temp=len(l1)-1
print("before printing",l1)
n=int(input("enter the number of shifiting"))
for i in range(n):
    for j in range(len(l1)-1):
        l1[i]=l1[i+1]
        temp=l1[i+1]
print("after shifting l1",l1)
