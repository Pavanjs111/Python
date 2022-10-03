from p1 import person
class student(person):
    def __init__(self, name, age, gender,percentage):
        super().__init__(name, age, gender)
        self.percentage=percentage