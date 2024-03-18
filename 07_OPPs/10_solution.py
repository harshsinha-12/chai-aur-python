class Car:
    total_cars = 0  

    def __init__(self, brand, model, color, year, price):
        self.brand = brand
        self.__model = model
        self.color = color
        self.year = year
        self.price = price
        Car.total_cars += 1

    def full_details(self):
        return f"{self.brand} {self.__model} {self.color} {self.year} {self.price}"
    
    def fuel_type(self):
        return "Uses Petrol or Diesel as fuel"
    
    @staticmethod
    def general_description():
        return "Cars are amazing!"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, color, year, price, battery_size):
        super().__init__(brand, model, color, year, price)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_electric_car = ElectricCar("Tesla", "Model S", "Red", "2021", "1500000", "100kWh")

class Battery:
    def battery_info(self):
        return f"The battery size of the car is {self.battery_size}"

class Engine:
    def engine_info(self):
        return f"The engine of the car is 1000cc"

class ElectricCar2(Battery, Engine, Car):
    def __init__(self, brand, model, color, year, price, battery_size):
        Car.__init__(self, brand, model, color, year, price)
        self.battery_size = battery_size

my_electric_car2 = ElectricCar2("Tesla", "Model S", "Red", "2021", "1500000", "100kWh")
print(my_electric_car2.battery_info())
print(my_electric_car2.engine_info())