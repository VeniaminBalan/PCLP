def custom_split(fraza, sep):
    cuvinte = []
    cuvant = ""
    for i in fraza:
        if i in sep:
            if cuvant != "":
                cuvinte.append(cuvant) 
            cuvant = ""
            continue
        cuvant += i
    else:
       if cuvant != "":
            cuvinte.append(cuvant)  
    return cuvinte

fraza = "Ana are 4 mere.,.,.,. 124"

for i in fraza.split(" "):
    print(i)

exit()

semne_de_punctuatie = {',', '.', '?', '!'}
vocale = {'a', 'e', 'i', 'o', 'u'}

numere = []
semne = []
cuvinte_cu_vocale = []
cuvinte_cu_consoane = []

for cuvant in custom_split(fraza, [' ', ',', '.']):
    if cuvant.isdecimal():
        numere.append(cuvant)
    for caracter in cuvant:
        if caracter in semne_de_punctuatie:
            semne.append(caracter)
    if cuvant.lower().startswith(tuple(vocale)):
        cuvinte_cu_vocale.append(cuvant)
    elif not cuvant.isdecimal():
        cuvinte_cu_consoane.append(cuvant)

    

print(f"numere gasite: {numere}")
print(f"semne de punctuatie gasite: {semne}")
print(f"cuvinte cu vocale gasite: {cuvinte_cu_vocale}")
print(f"cuvinte cu consoane gasite: {cuvinte_cu_consoane}")



