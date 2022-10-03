l1=[10,20,45,60,75,98,104,506]
max=l1[0]
for i in range (1,len(l1)):
    if max<l1[i]:
        max=l1[i]
print("the maximum of two number is ",max)
