while True:
    n : int = int(input("Enter a number: "))
    if n < 0 or n > 10:
        print("Number is not in range [0, 10]! Exiting.")
        break
    else:
        print("Number is in range [0, 10]. Try Again!")
        continue
