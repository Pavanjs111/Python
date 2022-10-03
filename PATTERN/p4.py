r=int(input())
c=int(input())
for i in range(r):
    val=c
    if val>9:
        val=9
    for j in range(c):
        print(val,end=" ")
        val-=1
        if val<1:
            val=9
    print()
    
       
    
