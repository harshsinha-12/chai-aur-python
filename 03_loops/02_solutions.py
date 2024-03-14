n : int = int(input("Enter the upper limit: "))
s_even : int = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s_even += i
print(f"Sum of even numbers is: {s_even}")
