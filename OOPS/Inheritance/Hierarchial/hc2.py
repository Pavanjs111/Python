from hp1 import car
class RR(car):
    steering="power"
    cc=1800
    gear=4
    def __init__(self,color,seating) -> None:
        super().__init__()
        self.color=color
        self.seating=seating
RR1=RR("yellow",4)
RR1.start()
