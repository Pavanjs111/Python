'''n=int(input())
if (n>>1)<<1==n:
    print(f"{n} is even")
else:
    print(f"{n} is odd")'''

n=int(input())
if (n>>1)<<1==n-1:
    print(f"{n} is odd")
else:
    print(f"{n} is even")