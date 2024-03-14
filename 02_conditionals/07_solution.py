coffee_size : str = input("What size coffee would you like? (Small, Medium, Large): ").capitalize()
extra_shot : str = input("Would you like an extra shot? (Y/N): ").upper()

if extra_shot == 'Y':
    coffee = coffee_size + ' Coffee' + ' with an extra shot'
    print(coffee)
else:
    coffee = coffee_size + ' Coffee'
    print(coffee)
