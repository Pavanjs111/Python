l1=[10,20,30,40,50]
it_1=iter(l1)
while True:
    try:
        num=next(it_1)
        print(num)
    except StopIteration:
        break