dist : int = int(input("Enter the distance in km: "))
if dist < 3:
    print("Walk")
elif dist < 15:
    print("Bike")
else:
    print("Car")