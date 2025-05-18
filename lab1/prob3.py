def read_input() -> tuple:
    try:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        z = int(input("Enter z: "))
    except Exception as e:
        print("Invalid input")
        return (0, 0, 0), e
    return (x, y, z), None

def max_of_three_numbers(x: int, y: int, z: int) -> int:
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    return z

def max(list : list[int]) -> int:
    #list.sort()
    sorted_list = sorted(list)
    return sorted_list[-1]

def min(list : list[int]) -> int:
    sorted_list = sorted(list)
    return sorted_list[0]

def main():
    input, err = read_input()

    if err:
        print(input)
        return
    
    print("The input is: ", input)
    list = [input[0],input[1],input[2]]

    print("before max function")
    print(list)
    print("The max of the three numbers is: ", max(list))
    print("after max function")    
    print(list)


if __name__ == "__main__":
    main()