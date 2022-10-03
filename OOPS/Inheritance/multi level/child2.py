from child1 import whatsappv2
class whatsappv3(whatsappv2):
    file_size=30
    def __init__(self, name, mno, about):
        super().__init__(name, mno, about)
    
    def audiomessage(self):
        print("calling...")

o2=whatsappv3("Pavan",7406030144," getting RICH")
print(o2.file_size)
print(o2.about)