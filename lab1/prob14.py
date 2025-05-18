def number_to_array(n: int) -> list:
    return [int(x) for x in str(n)]

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        print(f"calclating {i}")
        a, b = b, a + b

def fibonacci2(n):
    fib_numbers = []
    a, b = 0, 1
    for i in range(n):
        fib_numbers.append(a)
        print(f"calclating {i}")
        a, b = b, a + b
    return fib_numbers



def main():
    for i in fibonacci2(100) :
        if i > 100:
            break

    print(i)


if __name__ == "__main__":
    main()