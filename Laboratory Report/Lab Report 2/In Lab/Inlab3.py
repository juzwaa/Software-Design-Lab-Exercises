class Car:
    def __init__(self, color, plate):
        self.color = color
        self.mileage = plate

    def __str__(self):
        return 'A {self.color} car'.format(self=self)

car_A = Car ('Blue', 1234)
print(car_A)