s1="abc"
s2="xyz"
s3=" "
for i in range(len(s1)):
    s3+= s1[i]+s2[len(s2)-i-1]
print(s3)