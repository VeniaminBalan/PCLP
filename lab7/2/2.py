from datetime import datetime

def citeste_matrice(fisier):
    with open(fisier, 'r') as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    matrice = [list(map(int, line.strip().split())) for line in lines[1:n+1]]
    return matrice, n

def scrie_out(fisier, titlu, valori):
    with open(fisier, 'a', encoding='utf-8') as f:
        f.write(f"\n{titlu}:\n")
        for val in valori:
            f.write(' '.join(map(str, val)) + '\n')

def extrage_elemente(matrice, n):
    diag_principala = [[matrice[i][i]] for i in range(n)]
    diag_secundara = [[matrice[i][n - 1 - i]] for i in range(n)]
    sub_diag_principala = [[matrice[i][j] for j in range(i)] for i in range(1, n)]
    peste_diag_principala = [[matrice[i][j] for j in range(i + 1, n)] for i in range(n - 1)]
    sub_diag_secundara = [[matrice[i][j] for j in range(n - i, n)] for i in range(1, n)]
    peste_diag_secundara = [[matrice[i][j] for j in range(0, n - 1 - i)] for i in range(n - 1)]

    colturi = [
        [matrice[0][0], matrice[0][n-1]],
        [matrice[n-1][0], matrice[n-1][n-1]]
    ]

    margini = []
    margini.append(matrice[0])              # sus
    for i in range(1, n - 1):               # laterale
        margini.append([matrice[i][0]] + ['...'] + [matrice[i][n - 1]])
    margini.append(matrice[n - 1])          # jos

    nord = [matrice[i] for i in range(n // 2)]
    sud = [matrice[i] for i in range((n + 1) // 2, n)]
    vest = [[matrice[i][j] for j in range(n // 2)] for i in range(n)]
    est = [[matrice[i][j] for j in range((n + 1) // 2, n)] for i in range(n)]

    return {
        "Diagonala principală": diag_principala,
        "Diagonala secundară": diag_secundara,
        "Sub diagonala principală": sub_diag_principala,
        "Peste diagonala principală": peste_diag_principala,
        "Sub diagonala secundară": sub_diag_secundara,
        "Peste diagonala secundară": peste_diag_secundara,
        "Colțurile matricei": colturi,
        "Marginile matricei": margini,
        "Zona nordică a matricei": nord,
        "Zona sudică a matricei": sud,
        "Zona vestică a matricei": vest,
        "Zona estică a matricei": est,
    }

def scrie_timp_modificare(fisier):
    with open(fisier, 'a', encoding='utf-8') as f:
        now = datetime.now()
        f.write(f"\nFișier modificat la: {now}\n")

def main():
    in_file = 'in.txt'
    out_file = 'out.txt'

    matrice, n = citeste_matrice(in_file)

    with open(out_file, 'w', encoding='utf-8'):  # reset content
        pass

    rezultate = extrage_elemente(matrice, n)

    for titlu, valori in rezultate.items():
        scrie_out(out_file, titlu, valori)

    scrie_timp_modificare(out_file)

if __name__ == '__main__':
    main()
