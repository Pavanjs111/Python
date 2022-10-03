n=int(input())
last=n%10
while(n>9):
    n=n//10

print(f"{last} is the last number")
print(f"{n} is the first number")
