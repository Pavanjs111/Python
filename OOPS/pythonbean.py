
class one:
    
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setMarks(self,marks):
        self.__marks=marks
    def getMarks(self):
        return self.__marks

obj=one()
obj.setName(name=input("enter the name"))
obj.setMarks(marks=int(input("enter the marks")))
a=obj.getName()
b=obj.getMarks()
print(a,b)