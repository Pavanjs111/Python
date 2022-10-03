import json
from queue import Empty
emp_details='{"emp_id":1234,"name":"jenny","phone":798456213,"address":"Bangalore"}'
print(type(emp_details))

emp_info=json.loads(emp_details)

print(type(emp_info))
for i,j in emp_info.items():
    print(i,j)