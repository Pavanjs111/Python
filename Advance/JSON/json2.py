import json
fh=None
try:
    fh=open("college.json","r")
    print(fh)
    institute_info=json.load(fh)
    print(type(institute_info))
    print(institute_info)
    
    print(institute_info('placements'))
    for i,j in institute_info.items():
            print(i,j)

except:
    print("handling error")
    print("no such file")

