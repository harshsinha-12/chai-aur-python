class Car:
    def __init__(self, brand, model, color, year, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price

my_car = Car("BMW", "X5", "Black", "2019", "1000000")

print(my_car.brand)
print(my_car.model)
print(my_car.color)
print(my_car.year)
print(my_car.price)

my_new_car = Car("Audi", "A6", "White", "2020", "1200000")

print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.color)
print(my_new_car.year)
print(my_new_car.price)