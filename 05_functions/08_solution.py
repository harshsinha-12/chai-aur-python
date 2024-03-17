def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

def main():
    print_kwargs(name="harsh", age=20)
    print_kwargs(name="john", age=30, city="new york")
    print_kwargs(name="jane", age=25, city="san francisco", country="usa")

main()