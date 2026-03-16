
class Car: 

    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model 
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod 
    def general_desc():
        return 'cars are means of transport'
    @property # we can use this def as property # to read only
    def model(self):
        return self.__model
    

class Battery:

    def battery_info(self):
        return "this is battery"

class Engine:

    def engine_info(self):
        return "this is engine"

class ElectricCar(Battery, Engine, Car):
    pass

my_electric_car = ElectricCar("brand", "model")
print(my_electric_car.battery_info())
print(my_electric_car.engine_info())