
months_days = {
    "January": 31,
    "February": 28,  # 29 in leap years
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def get_months(n: int) -> dict:
    dic = dict()

    if n == 29:
        dic["February(leap years)"] = 29

    for month, days in months_days.items():
        if days == n:
            dic[month] = days

    return dic

def get_n() -> int:
    while True:
        try:
            n = int(input("Enter n: "))
            if(n >= 28 and n <= 31):
                return n
            else:
                print("Invalid input. Please enter a value between 28 and 31.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for n.")


def ensure_input():
    n = input("Enter n: ")
    while not n.isdigit():
        print("Invalid input. Please enter a numeric value for n.")
        n = input("Enter n: ")
    return int(n)
    


def main():

    n = ensure_input()

    for month, days in get_months(n).items():
        print(f"{month}: {days} days")

    pass




if __name__ == "__main__":
    main()