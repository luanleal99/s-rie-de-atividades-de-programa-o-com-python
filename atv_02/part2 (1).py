import sys


def explorar(matriz, linha, coluna):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if matriz[linha][coluna] != 1:
        return 0

    tamanho = 1

    # Conta 1s continuos para CIMA
    l = linha - 1
    while l >= 0 and matriz[l][coluna] == 1:
        tamanho += 1
        l -= 1

    # Conta 1s continuos para BAIXO
    l = linha + 1
    while l < linhas and matriz[l][coluna] == 1:
        tamanho += 1
        l += 1

    # Conta 1s continuos para ESQUERDA
    c = coluna - 1
    while c >= 0 and matriz[linha][c] == 1:
        tamanho += 1
        c -= 1

    # Conta 1s continuos para DIREITA
    c = coluna + 1
    while c < colunas and matriz[linha][c] == 1:
        tamanho += 1
        c += 1

    return tamanho


def analisar(matriz):
    maior_regiao = 0
    posicao = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tamanho = explorar(matriz, i, j)
            if tamanho > maior_regiao:
                maior_regiao = tamanho
                posicao = (i, j)

    return (maior_regiao, posicao)


# Estude a parte a seguir.
# Não modifique nada a partir daqui

def main(argv):
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
        with open(inputfile, "r") as f:
            matriz = [list(map(int, linha.split())) for linha in f]
        print(analisar(matriz))

if __name__ == "__main__":
    main(sys.argv)