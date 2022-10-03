n1=int(input("n1:"))
n2=int(input("n2:"))
print("before swapping")
print("n1={}\tn2={}".format(n1,n2))
n1=n1*n2
n2=n1//n2
n1=n1//n2
print("after swapping")
print("n1={}\tn2={}".format(n1,n2))