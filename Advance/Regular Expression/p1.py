import re
str1="I am devil in my world and I am here for bad guys to kill"
pat="kill"
res=re.search(pat,str1)
if res!=None:
    print("match found")
    print("match found at ",res.span())
else:
    print("match not found")