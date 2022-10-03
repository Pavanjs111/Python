s1="I_Am_King_For_My_Forest"
s2=" "
for i in range(len(s1)):
    if ord(s1[i])>=65 and ord(s1[i])<=90:
        s2=s2+chr(ord(s1[i])+32)
    elif s1[i]=="_":
        s2=s2+" "
    else:
        s2=s2+s1[i]
print(s2)