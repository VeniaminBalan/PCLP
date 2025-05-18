from fractions import Fraction

def generate_multiplication(n: int) -> int:
    prodcut = 1
    for i in range(1, n+1):
        prodcut = prodcut * i
    return prodcut

def generate_odds_multiplication(n: int) -> int:
    prodcut = 1
    for i in range(1, 2*n+2, 2):
        print(i)




def main():

    n = int(input("Enter a number: "))

    generate_odds_multiplication(n)
    e = sum([Fraction(1 , generate_multiplication(i))  for i in range(1, n+1)])

    print(f"e = {float(e)}")

    pass




if __name__ == "__main__":
    main()