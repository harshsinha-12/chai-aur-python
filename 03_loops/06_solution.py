n : int = int(input("Enter the number for factorial: "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1
print(fact)
