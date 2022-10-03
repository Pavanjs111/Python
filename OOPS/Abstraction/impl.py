from abc import ABC
from p1 import calculate
class logic(calculate):
    def add(self,*arg):
        sum=0
        for i in arg:
            sum+=i
        print(sum)

    def mul(self,*arg):
        pro=1
        for i in arg:
            pro*=i
        print(pro)
        