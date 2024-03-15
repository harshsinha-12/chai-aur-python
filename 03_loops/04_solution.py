str = input("Enter a string: ")
reversed_str = ""
for i in range(len(str)):
    reversed_str += str[-i-1]
print(reversed_str)