r=int(input())
c=int(input())
val=ord('A')
for i in range(r):
    for j in range(c):
        print(chr(val),end=" ")
        val+=1
        if val>ord('Z'):
            val=ord('A')
    print()
    val=ord('A')
