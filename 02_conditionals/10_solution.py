species : str = input("Enter the species: ").capitalize()
age : int = int(input("Enter the age: "))
if species == "Dog":
    if age < 2:
        print("Puppy Food")
    elif age < 5:
        print("Adult Food")
    else:
        print("Senior dog food")
elif species == "Cat":
    if age < 2:
        print("Kitten Food")
    elif age < 5:
        print("Cat Food")
    else:
        print("Senior cat food")