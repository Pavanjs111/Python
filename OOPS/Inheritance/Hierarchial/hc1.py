from hp1 import car
class benz(car):
    steering="power"
    cc=1800
    gear=4
    def __init__(self,color,seating) -> None:
        super().__init__()
        self.color=color
        self.seating=seating
benz1=benz("blue",4)
benz1.wheel