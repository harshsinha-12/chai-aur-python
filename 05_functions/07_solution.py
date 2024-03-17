def sum_all(*args : float) -> float:
    return sum(args)


def main():
    print(sum_all(2, 3, 4))
    print(sum_all(3, 4, 5))
    print(sum_all(4, 5, 6))

main()