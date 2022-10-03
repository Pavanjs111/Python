class one:
    __a=100

    def __fun(self):
        print("fun of one")
        print("value of a is",self.__a)
        
    def fun(self):
        self.__fun()

o=one()
o.fun()