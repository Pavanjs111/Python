l1=[10,20,35,46,12,15,84]
max1=l1[0]
max2=l1[1]
for i in range (2,len(l1)):
    if max1<l1[i]:
        max2=max1
        max1=l1[i]
    elif max2<l1[i]:
        max2=l1[i]
print("the first max and second max is",max1,max2)

