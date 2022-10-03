row=int(input("enter the number of row"))
col=int(input("enter the number of col"))

print("enter the elements of matrix 1:")
matrix1=[[int(input()) for j in range(col)]for i in range(row)]

print("matrix 1")
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

print("enter the elements for matrix2")
matrix2=[[int(input()) for j in range(col)]for i in range(row)]

print("matrix 1")
for i in range(row):
    for j in range(col):
        print(matrix2[i][j],end=" ")
    print()

res=[[0 for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        res[i][j]=matrix1[i][j]-matrix2[i][j]

print("Result is:")
for i in range(row):
    for j in range(col):
        print(res[i][j],end=" ")
    print()
