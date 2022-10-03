def gen_num():
    print("function returning for the first time")
    yield 10
    print("function running for the second time ")
    yield 20
    print("function running for the third time")
    yield 30
    
gens=gen_num()
print(gens)
print(type(gens))
print(dir(gens))
print(next(gens))
print(next(gens))
print(next(gens))
