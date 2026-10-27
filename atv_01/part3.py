import sys


def maior_sequencia_crescente(valores):
    if len(valores) == 0:
        return (0, 0)

    maior_tam = 1
    maior_pos = 0

    tam_atual = 1
    pos_atual = 0

    for i in range(1, len(valores)):
        if valores[i] > valores[i - 1]:
            tam_atual = tam_atual + 1
        else:
            if tam_atual > maior_tam:
                maior_tam = tam_atual
                maior_pos = pos_atual

            tam_atual = 1
            pos_atual = i

    if tam_atual > maior_tam:
        maior_tam = tam_atual
        maior_pos = pos_atual

    return (maior_tam, maior_pos)


# Estude a parte a seguir.
# Não modifique nada a partir daqui

if len(sys.argv) > 1:
    inputfile = sys.argv[1]
    with open(inputfile, "r") as f:
        valores = list(map(int, f.read().split()))
        resultado = maior_sequencia_crescente(valores)
        print(resultado)