from hashlib import sha256


s1="I am Iron man and I am inevitable"
s2=s1.split()
print(s2)
s3=s1.split("I",1)
s4=s1.split("Iron")
print(s3)
print(s4)
s5=s1.split(" ",5)
print(s5)