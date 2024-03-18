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

# init method is called automatically when a new object is created
# self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
# __init__ method is used to initialize the object's state
# __init__ method is called constructor method in Python
# class is a blueprint for creating objects
# object is an instance of a class
# class is a collection of objects
# object is a collection of variables and methods
# class is a collection of variables and methods
# method is a function that belongs to a class