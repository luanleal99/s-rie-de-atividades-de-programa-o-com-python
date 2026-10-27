import sys


def ordenar_atividades(atividades):
    n = len(atividades)
    for i in range(n):
        for j in range(0, n - i - 1):
            if atividades[j][2] > atividades[j + 1][2]:
                atividades[j], atividades[j + 1] = (
                    atividades[j + 1],
                    atividades[j],
                )
    return atividades


def compativel(a, b):
    return b[1] >= a[2]


def selecionar(atividades):
    atividades_ordenadas = ordenar_atividades(atividades)
    selecionadas = []

    if len(atividades_ordenadas) == 0:
        return selecionadas

    atual = atividades_ordenadas[0]
    selecionadas.append(atual)

    for i in range(1, len(atividades_ordenadas)):
        proxima = atividades_ordenadas[i]
        if compativel(atual, proxima):
            selecionadas.append(proxima)
            atual = proxima

    return selecionadas


# Estude a parte a seguir.
# Não modifique nada a partir daqui

def main(argv):
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

        with open(inputfile, "r") as f:
            atividades = []

            for linha in f:
                nome, inicio, fim = linha.split()
                atividades.append((nome, int(inicio), int(fim)))

            resultado = selecionar(atividades)
            for v in resultado:
                print (v[0])


if __name__ == "__main__":
    main(sys.argv)