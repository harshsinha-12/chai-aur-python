class Car:
    def __init__(self, brand, model, color, year, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def full_details(self):
        return f"{self.brand} {self.model} {self.color} {self.year} {self.price}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, color, year, price, battery_size):
        super().__init__(brand, model, color, year, price)
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Model S", "Red", "2021", "1500000", "100kWh")
print(my_electric_car.full_details())