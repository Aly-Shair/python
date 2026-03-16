class Car: # is class ko ik seperate file ma bana kar rakh do jab bhi use karna ha isko import kara lein gay

    # brand = None
    # model = None

    # def __init__(self, user_brand, user_model): 
    #     brand = user_brand
    #     model = user_model

    def __init__(self, brand, model): # self is necessary # __init__ is a contructor
        self.brand = brand # self is necessary
        self.model = model # self is necessary

my_car = Car("Toyota", "Corolla")
print(my_car)
print(my_car.brand)
print(my_car.model)