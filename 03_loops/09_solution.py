items = ["apple", "banana", "orange", "apple", "mango"]

for i in range(len(items)):
    if items[i] in items:
        print(f"{items[i]} is a duplicate.")
        break
    else:
        print("No duplicates found.")