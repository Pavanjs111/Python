import re
email="walter@breakingbad.com"
term_to_split='b'
res=re.split(term_to_split,email)
print(res)