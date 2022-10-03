import re
data="develop"
data1="Khiladi420"
res=re.search("Khila[a-z][a-z][0-9]20",data1)
if res!=None:
    print("match found")
else:
    print("match not found")