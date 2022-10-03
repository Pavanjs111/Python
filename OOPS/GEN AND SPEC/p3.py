from p1 import person
class teacher(person):
    def __init__(self, name, age, gender,salary):
        super().__init__(name, age, gender)
        self.salary=salary

        