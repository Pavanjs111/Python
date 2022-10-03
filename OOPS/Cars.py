class  cars:
    tyres=4
    camera=1
    seats=4
    
    def __init__(self,year,name,nplate,speed,color,size,oname):
        self.year=year
        self.name=name
        self.nplate=nplate
        self.speed=speed
        self.color=color
        self.size=size
        self.oname=oname

    def fun(self):
        print("Car is on the road")

    
    def info(self):
        print(f"{self.year} :bought")
        print(f"{self.name} : model")
        print(f"{self.nplate}: plate")
        print(f"{self.speed} :speed")
        print(f"{self.color} :color")
        print(f"{self.size} :size")
        print(f"{self.oname} :is the owner of the car")

car1=cars(2022,"Aventador","KA046969",400,"Blue","Big","Pavan")
car2=cars(2022,"RR","KA041313",350,"white","Big","Jishnu")
car3=cars(2022,"Tata Nano","KA046347",250,"green","small","Ajay")
car4=cars(2022,"Benz","KA046759",450,"Yellouw","Big","Prithvi")

car1.info()
car1.fun()
print(f"tyres={cars.tyres},seats={cars.seats},cameras={cars.camera}")
print("**********************")
car2.info()
car2.fun()
print(f"tyres={cars.tyres},seats={cars.seats},cameras={cars.camera}")
print("**********************")
car3.info()
print(f"tyres={cars.tyres},seats={cars.seats},cameras={cars.camera}")
print("**********************")
car4.fun()
car4.info()
print(f"tyres={cars.tyres},seats={cars.seats},cameras={cars.camera}")