l1=[1,2,3,4,5]
print(type(l1))
# print(dir(l1))
# for i in l1:
#     print([i])


# print(next(l1))
iter_l1=l1.__iter__()
print(dir(iter_l1))
print(next(iter_l1))
print(next(iter_l1))
print(next(iter_l1))
print(next(iter_l1))
print(next(iter_l1))
