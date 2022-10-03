from parent import whatsappv1
class whatsappv2(whatsappv1):

    def __init__(self, name, mno,about):
        super().__init__(name, mno,)
        self.about=about

    def voicemessage(self):
        print("click here to record")
    
o1_whatsappv2=whatsappv2("Jishnu",7406030145,"I will be back soon")
o1_whatsappv2.chat()
print(o1_whatsappv2.about)