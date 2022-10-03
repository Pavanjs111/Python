''' row=int(input("enter row:"))
col=int(input(" enter col:"))
val=1
for i in range (row):
    for j in range(col):
        print(val,end=" ") 
        val+=1
        if val>9:
            val=1
    print()'''

row=int(input("enter row:"))
col=int(input(" enter col:"))
val=1

for i in range (row):
    for j in range(col):
        print(val,end=" ")     
    print()
    
    val+=1
    if val>9:
        val=1