n1=int(input())
n2 =int(input())
max=0
min=0
if n1==n2:
    print(f"{n1} and {n2} are same")
else:
        if n1>n2:
            max=n1
            min=n2
        else:
                max=n2
                min=n1
                print(f"{max} is maximum and {min} is minimum")

