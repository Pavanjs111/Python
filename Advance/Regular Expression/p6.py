import re
data1="Khiladi420"
res=re.search("Khi..di..0",data1)
if res!=None:
    print("match found")
else:
    print("match not found")