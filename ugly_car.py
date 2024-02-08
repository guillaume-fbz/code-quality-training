import this
import random
import pytest

class car:
    def __init__(self,make,car,year,speed):
        self.make=make
        self.model=car
        self.year=year
        self.speed=speed

    def start(self):
        print("Car started!")

    def accelerate(self, increment):
        self.speed+=increment

    def brake(self, decrement):
        self.speed -= decrement

    def display_info(self):
        print(f"Vendor: {self.make}")

    def long_method(cls):
        print("The Peugeot 206 is a popular and compact car model known for its stylish design, efficient performance.")

    def __str__(self):
        return f'This is a car: {self.year} {self.make} {self.model}'

car_radio_code = 1337

myCar = car("Peugeot", "206", 1998, 0)

myCar.start()
myCar.accelerate(20)
myCar.brake(5)
myCar.display_info()

myCar_description = "This car is beautiful :)"

exec("hello !")

print(myCar)
