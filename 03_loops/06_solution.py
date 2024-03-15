a = 0
b = 1
n : int = int(input("Enter the upper limit: "))
while a < n:
    print(a)
    a, b = b, a+b
