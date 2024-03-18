class Car:
    def __init__(self, brand, model, color, year, price):
        self.__brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def get_brand(self):
        return self.__brand + "! "

    def full_details(self):
        return f"{self.__brand} {self.model} {self.color} {self.year} {self.price}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, color, year, price, battery_size):
        super().__init__(brand, model, color, year, price)
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Model S", "Red", "2021", "1500000", "100kWh")
#print(my_electric_car.__brand)
print(my_electric_car.get_brand())