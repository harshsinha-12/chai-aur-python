pwd : str = input("Enter the password: ")
if len(pwd) < 6:
    print("Password is Weak")
elif len(pwd) < 10:
    print("Password is Medium")
else:
    print("Password is Strong")

