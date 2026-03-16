class Car: 

    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model 
        # self.total_cars += 1 # wrong
        Car.total_cars += 1 # right

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod # they are also called decorators # jab static method banatay ho to self to nahi likhna ha
    def general_desc():
        return 'cars are means of transport'
    
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"


# my_car_2 = ElectricCar("tesla", "Model S", "85kwh")
# my_car_1 = Car("toyota", 'corolla')

# print(my_car_1.general_desc())  # error

print(Car.general_desc()) 
print(ElectricCar.general_desc()) 