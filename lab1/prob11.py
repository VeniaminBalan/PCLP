def read_student() -> tuple:
    name = input("Enter name: ")
    grade = float(input("Enter grade: "))
 
    return (name, grade)


def main():
    #name1, grade1 = read_student()
    #name2, grade2 = read_student()
    #name3, grade3 = read_student()

    dic = {
        "Ab a": 5, 
        "Ab c": 5,
        "Ab": 7,
        "B": 5,
        "Cb": 10,
        "Ca" : 10
        }
    
    res = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])) )

    {print(f"{item[0]}: {item[1]}") for item in res.items()}

    pass

if __name__ == "__main__":
    main()