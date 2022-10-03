import re
msg="I dont Know my Name"
pat='my'
res=re.findall(pat,msg)
if res!=None:
    print("found at ->", res.span())
else:
    print("not found")