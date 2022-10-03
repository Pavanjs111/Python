class animals:
    type1="Birds"
    type2="Reptiles"
    type3="Mammals"
    type4="Amphibians"

    def __init__(self, ftype,name,color,speed,legs,region):
        self.ftype=ftype
        self.name=name
        self.color=color
        self.speed=speed
        self.legs=legs
        self.region=region

    def info(self):
        print(f"type:{self.ftype}")
        print(f"name:{self.name}")
        print(f"colore:{self.color}")
        print(f"speed:{self.speed}")
        print(f"legs:{self.legs}")
        print(f"region:{self.region}")

    def land(self):
        print("Live on Land")
    
    def water(self):
        print("Live in water")
    
    def both(self):
        print("Live in both land and water")

    def fly(self):
        print("Is able to fly")

o_1=animals("carnivores","Eagle","Brown",50,2,"sky")
o_2=animals("Herbivores","Cow","Black and white",5,4,"grasslands")
o_3=animals("carnivores","Lion","Yellow",80,4,"forests")
o_4=animals("carnivores","Croc","darkgreen",25,4,"water")
       

o_1.info()
o_1.fly()
o_1.land()
o_1.type1
print("###########################")
o_2.info()
o_2.land()
o_2.type3
print("###############################")
o_3.info()
o_3.land()
o_3.type3
print("*****************************")
o_4.info()
o_4.both()
o_4.type4 and o_4.type2

