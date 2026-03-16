# class Car: 

#     total_cars = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model 
#         Car.total_cars += 1

#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
    
#     def fuel_type(self):
#         return "petrol or diesel"
    
#     @staticmethod 
#     def general_desc():
#         return 'cars are means of transport'
    
#     def model(self):
#         return self.__model
    
# class ElectricCar(Car):

#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "electric charge"


# my_car_1 = Car("toyota", 'corolla')

# my_car_1.model = "city"
# print(my_car_1.model)
# # print(my_car_1.model())












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
    
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"


my_car_1 = Car("toyota", 'corolla')
my_car_2 = ElectricCar("tata", 'safari', "85kwh")

print(my_car_1.model)
print(my_car_2.model)
