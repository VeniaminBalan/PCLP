def contine_vocale(cuvant, nr_vocale = -1):
    vocale_gasite = 0
    vocale = "aeiouăîâ"
    for litera in cuvant:
        if litera in vocale:
            vocale_gasite += 1

    if nr_vocale == -1:
        return vocale_gasite > 0

    if vocale_gasite == nr_vocale:
        return True
    
    return False


def subiect1_2():
    cuvinte = ["programare", "python", "cod", "lista", "exemplu", "test", "vocale", "cuvant"]

    print([i for i in cuvinte if contine_vocale(i, 2)])



# vector = [3, 6, 7, 14, 21, 42, 55, 110] 

# print([vector[j] for j in range(1,len(vector)) if vector[j] == vector[j-1] * 2] )

import numpy as np

vector = np.array([1, 2, 3,4,5])

lenght = vector.size

def parse(x:int, y: int, lenght: int):
    tmp = x + y
    if tmp >= lenght:
        return tmp - lenght
    return tmp

def parse2(x:int, lenght: int):
    if x >= lenght:
        return x - lenght
    return x
     
def shuffle(vector: np.ndarray):
    for i in range(1, len(vector)-1, 2):
        vector[i], vector[i + 1] = vector[i + 1], vector[i]
    return vector

# mat = np.zeros((lenght,lenght * 2), "i4")
# for i in range(lenght):
#     for j in range(lenght * 2):
#         mat[i,j] = vector[parse(i, parse2(j, lenght), lenght)]
#         pass
#     print()

# print()
# print(mat)

# v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(v)
# print(shuffle(v))


# def level(tuple: tuple, lenght: int) -> int:
#     x, y = tuple
#     v_level = 0
#     pass


# vector2 = np.array([1, 2, 3,4,5,6])

# lenght2 = vector2.size

# mat = np.zeros((lenght2 ,lenght2), "i4")
# for i in range(lenght2):
#     for j in range(lenght2):
#         print((i,j), end = " ")
#     print()
