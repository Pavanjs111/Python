n1=int(input("n1:"))
n2=int(input("n2:"))
n3=int(input("n3:"))
print("before swapping")
print("n1={}\tn2={}\tn3={}".format(n1,n2,n3))
n1=n1*n2*n3
n2=n1//(n2*n3)
n3=n1//(n2*n3)
n1=n1//(n2*n3)
print("after swapping")
print("n1={}\tn2={}\tn3={}".format(n1,n2,n3))