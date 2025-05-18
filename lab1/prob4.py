from math import sqrt

def find_x(a: int, b: int) -> float:
    return -b / a

def find_x(a: int, b: int, c: int) -> float | tuple | None:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return x1, x2


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    print("The value of x is: ", find_x(a, b, c))

    pass


if __name__ == "__main__":
    main()