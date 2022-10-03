# n= int(input())
# for i in range(1,n+1):
#         print((i*i)+1,end=" ")

n=int(input())
sq=1
for i in range(0,n+1):
    if (i%2!=0):
        print((sq*sq),end=" ")
        sq+=1
    else:
        print((sq*sq)-1,end=" ")
        
   