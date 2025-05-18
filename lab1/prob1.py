def is_even(number: int) -> bool:
    return number % 2 == 0

def main():

    input_number = int(input("Enter a number: "))

    if is_even(input_number):
        print("The number is even")
    else:
        print("The number is odd")

    

    pass



if __name__ == "__main__":
    main()