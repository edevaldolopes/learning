class Car:
    def __init__(self, brand, color, year, tank, wheel):
        self.brand = brand
        self.wheel = wheel
        self.color = color
        self.year = year
        self.tank = tank

    def fuel(self, liter):
        self.tank += liter


class Motorcycle(Car):
    def __init__(self, brand, color, year, tank, wheel):
        Car.__init__(self, brand, color, year, tank, wheel)

    def fuel(self, liter):
        if self.tank + liter > 35:
            print('Fail fuel')
        else:
            self.tank += liter


car1 = Car('uno', 'green', 1994, 45, 4)
car1.fuel(10)
print(car1.brand)
print(car1.wheel)
print(car1.color)
print(car1.year)
print(car1.tank)

moto1 = Motorcycle('honda', 'red', 2021, 25, 2)
moto1.fuel(50)
print(moto1.brand)
print(moto1.wheel)
print(moto1.color)
print(moto1.year)
print(moto1.tank)
