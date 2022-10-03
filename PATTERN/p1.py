row=int(input("enter row:"))
col=int(input(" enter col:"))
for i in range (row):
    val=1
    for j in range(col):
        print(val,end=" ") 
        val+=1
        if val>9:
            val=1
    print()
5
# row=int(input("enter row:"))
# col=int(input(" enter col:"))
# for i in range(row):
#     for j in range(col):
#         print("* ",end=" ") 
#     print()

