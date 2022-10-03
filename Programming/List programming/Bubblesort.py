l1=[10,2,12,1,20]
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print(l1)