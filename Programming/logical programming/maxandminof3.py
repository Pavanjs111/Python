'''n1 = int(input())
n2 = int(input())
n3 = int(input())
max=0
if n1==n2 and n2==n3:
    print(f"{n1} and {n2} and {n3} are same")
else:
    if n1>n2 and n1>n3:
         max=n1
    elif n2>n3:
        max=n2
    else:
        max=n3
        print(f"{max} is maximum ")'''

n1 = int(input())
n2 = int(input())
n3 = int(input())
min=0
if n1==n2 and n2==n3:
    print(f"{n1} and {n2} and {n3} are same")
else:
    if n1<n2 and n1<n3:
        min=n1
    elif n2<n3:
        min=n2
    else:
        min=n3
print(f"{min} is minimum ")