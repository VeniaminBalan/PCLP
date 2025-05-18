def is_pozitive(n):
    return n >> 31 == 0


def main():

    input_number = int(input("Enter a number: "))
    if is_pozitive(input_number):
        print("The number is pozitive")
    else:
        print("The number is negative")

    pass

if __name__ == "__main__":
    main()