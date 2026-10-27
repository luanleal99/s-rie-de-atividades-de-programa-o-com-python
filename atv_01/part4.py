import sys


def intervalos(valores):
    if len(valores) == 0:
        return []

    resp = []
    i = 0

    while i < len(valores):
        inicio = valores[i]
        j = i

        while j + 1 < len(valores) and valores[j + 1] == valores[j] + 1:
            j = j + 1

        fim = valores[j]

        resp.append((inicio, fim))

        i = j + 1

    return resp


# Estude a parte a seguir.
# Não modifique nada a partir daqui

if len(sys.argv) > 1:
    inputfile = sys.argv[1]
    with open(inputfile, "r") as f:
        valores = list(map(int, f.read().split()))
        resultado = intervalos(valores)
        print(resultado)

