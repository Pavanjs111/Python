# def mul_of_two(n):
#     if n%2==0:
#         return True
#     return False

# l1=[x for x in range(1,101)]
# print(l1)

# even_list=[]
# for i in l1:
#     if mul_of_two(i):
#         even_list.append(i)
# print(even_list)

# ===================================================================

# def mul_of_two(n):
#     if n%2==0:
#         return True
#     return False
# l1=[x for x in range(1,101)]
# print(l1)
# even_list=list(filter(mul_of_two,l1))
# print(even_list)

# ======================================================================

# l1=[x for x in range(1,101)]
# print(l1)
# even_list=list(filter(lambda n:n%2==0,l1))
# print(even_list)
# ========================================================================

# movies=["jackie","charlie","avengers","James Bond"]
# starts_with_c=list(filter(lambda n:n.startswith("c"),movies))
# print(starts_with_c)

fh=open("file.txt")
l1=fh.readlines()
a=input()
l2=list(filter(lambda n:n.startswith(a),l1))
fh.close()


f=open("file2.txt","w")
f.writelines(l2)
f.close()







































