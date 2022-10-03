l1=[10,20,45,60,75,98,104,506]
min=l1[0]
index=0
for i in range (1,len(l1)):
    if min>l1[i]:
        min=l1[i]
        index=l1[min]
print("the minimum of two number is and index is",min,index)