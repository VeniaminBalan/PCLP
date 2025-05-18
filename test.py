
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


cuvinte = ["programare", "python", "cod", "lista", "exemplu", "test", "vocale", "cuvant"]

print([i for i in cuvinte if contine_vocale(i, 2)])
print([i for i in cuvinte if contine_vocale(i, 3)])

