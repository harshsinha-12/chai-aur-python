def fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def main():
    print(fact(5))

main()