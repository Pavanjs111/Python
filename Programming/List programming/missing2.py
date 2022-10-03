l1=[8,20,1,24,30]
for i in range(0,len(l1)-1):
    fe=l1[i]+1
    le=l1[i+1]
    if fe>le:
        for i in range(fe-2,le,-1):
            print(i,end=" ")
    else:
        for i in range (fe,le):
            print(i,end=" ")