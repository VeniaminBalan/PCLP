def isNumber(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    nota_examen  = int(input("Nota examen: ")) 
    match (nota_examen): 
        case 1|2|3|4: 
            print("Mai trebuie sa invat") 
        case 5|6|7|8|9: 
            print("Am trecut, dar vin la marire!") 
        case 10: 
            print("Sunt TARE") 
        case _: 
            print("{} nu este nota!".format(nota_examen)) 

if __name__ == "__main__":
    main()