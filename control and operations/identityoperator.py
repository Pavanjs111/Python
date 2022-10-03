a=10
b=500
c=10
print(a is b)
print(c is b)
print(a is c)

a=900
b=350
c=800
d=900
e=350
print(a is d)
print(a is e)
print(a is b)
print(b is e)
print(c is d)


a=-900
c=850
b=-900
d=-300
f=-300
print(a is c)
print(d is f)
print(a is b)