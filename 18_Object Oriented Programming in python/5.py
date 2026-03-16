class Car: 

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model 

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"

my_car = Car("toyota", 'corolla')
print(my_car.fuel_type())

my_tesla = ElectricCar("tesla", "Model S", "85kwh")
print(my_tesla.fuel_type())