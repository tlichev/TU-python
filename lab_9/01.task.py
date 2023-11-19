import json

class Car:
    def __init__(self,brand, model, power, mileage ):
        self.brand = brand
        self.model = model
        self.power = power
        self.mileage = mileage


    def print_info(self):
        print(f"{self.brand},{self.model},{self.power},{self.mileage}")

car1 = Car("BMW", "320d", "163", "300000")

json_car = json.dumps(car1.__dict__)
print(json_car)



