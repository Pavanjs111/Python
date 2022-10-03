from p2 import student
from p3 import teacher
class govt_services():
    def scholarship(self,obj):
        if isinstance(obj,student):
            if obj.percentage>=65:
                print("eligible for scholarship")
            else:
                print("not eligible")
        else:
            print("Data mismatched")

    def tax(self,obj):
        if isinstance(obj,teacher):
            if obj.salary>5:
                print("Has to pay tax ",0.1*obj.salary)
            else:
                print("no tax")
        else:
            print("record mismatched")
    
    def voterid(self,obj):
        if obj.age>18:
            print("eligible to vote")
        else:
            print("not eligible")

o1=govt_services()
o2=student("Pavan",22,"male",65)
o1.scholarship(o2)
o3=teacher("Irshan",27,"male",30)
o1.tax(o3)
o1.voterid(o2)
o1.voterid(o3)
