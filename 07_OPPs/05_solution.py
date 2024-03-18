class Car:
    def __init__(self, brand, model, color, year, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def full_details(self):
        return f"{self.brand} {self.model} {self.color} {self.year} {self.price}"
    
    def fuel_type(self):
        return "Uses Petrol or Diesel as fuel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, color, year, price, battery_size):
        super().__init__(brand, model, color, year, price)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_electric_car = ElectricCar("Tesla", "Model S", "Red", "2021", "1500000", "100kWh")

safari = Car("Tata", "Safari", "White", "2021", "2000000")
print(safari.fuel_type())
print(my_electric_car.fuel_type())