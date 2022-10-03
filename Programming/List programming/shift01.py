l1=[0,0,1,0,0,1,1,0,0,1,0]
print("before shifting",l1)
zc=0
for i in range (len(l1)):
    if l1[i]==0:
        zc+=1
for i in range(len(l1)):
    if i<zc:
        l1[i]=0
    else:
        l1[i]=1
print("After shifting",l1)
