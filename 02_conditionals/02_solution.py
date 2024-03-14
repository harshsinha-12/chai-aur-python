age = int(input('Enter your age: '))
day = input('Enter the day of the week: ')

price = 0

if age >= 18:
    price = 12
else:
    price = 8

if day == 'Wednesday':
    price = price - 2

print(f'The price is ${price}')

