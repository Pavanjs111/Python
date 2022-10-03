#logical operator
a=10
b=20
c=10
print(a==b and b>10)
print(a==c and b==a)
print(a==c and b>10)
print(a>=c and b>=a)
print(a==b or b==c)
print(a>b or b>c)
print(a>b or b<c)
print(not(a==c))
print(not(a>b))


#ASSIGNMENT OPERATOR
a=10
b=20
a+=50
print(a,b)

a=6
b=3
b+=200
print(a,b)

a=50
b=3
a*=50
b*=3
print(a,b)


#BITWISE OPERATOR
a=13
b=5
print(a&b)

a=6
b=56
print(a|b)

a=45
b=12
print(a^b)