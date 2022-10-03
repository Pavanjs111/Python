l1=['n','#','i','@','v','!','a','*','n']
for i in range(len(l1)):
    if l1[i]>='a' and l1[i]<='z' or l1[i]>='1' and l1[i]<='9':
        temp=l1[i]
        l1[i]=l1[(len(l1)-1)-i]
        l1[len(l1-1)]=temp
print(l1)