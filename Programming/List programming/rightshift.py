l1=[1,2,3,4,5]
print("before rotation->",l1)
temp=l1[len(l1)-1]

for i in range(len(l1)-1,-1,-1):
    l1[i]=l1[i-1]
l1[0]=temp

print("After rotaion->",l1)