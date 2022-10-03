a=int(input("Enter the number of rows"))
b=int(input("enter the number od columns"))
mat=[]

for i in range (a):
    c=[]
    for j in range(b):
        val=int(input("Enter the values for index   "+str(i)+" "+str(j)+" "))
        c.append(val)
    print()
    mat.append(c)

for i in range(a):
    for j in range(b):
        print(mat[i][j],end=" ")
    print()