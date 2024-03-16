def cir_area(radius : float) -> float:
    area = 3.14 * radius ** 2
    cir = 2 * 3.14 * radius
    return area, cir

def main():
    print(cir_area(2))
    print(cir_area(3))
    print(cir_area(4))

main()
