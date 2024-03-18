class Car:
    def __init__(self, brand, model, color, year, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def full_details(self):
        return f"{self.brand} {self.model} {self.color} {self.year} {self.price}"

my_car = Car("BMW", "X5", "Black", "2019", "1000000")

print(my_car.full_details())

my_new_car = Car("Audi", "A6", "White", "2020", "1200000")

print(my_new_car.full_details())