s1="Radhe"
s2="Shyam"
s3=""
for i in range(len(s1)):
    if i<len(s1)//2:
        s3=s3+s1[i]
    elif i==len(s1)//2:
        for j in range(len(s2)):
            s3=s3+s2[j]
        s3=s3+s1[i]
    else:
        s3=s3+s1[i]
print(s3)
        
