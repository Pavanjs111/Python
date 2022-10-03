import re
str1="I am not in danger  I am the danger now say my name"
patterns=["danger","naem","devil","say"]
for pat in patterns:
    print("searching for pattern pat->",pat)
    res=re.search(pat,str1)
    if res!=None:
        print("match found")
        print("patter found at",res.span())
    else:
        print("pattern not found")