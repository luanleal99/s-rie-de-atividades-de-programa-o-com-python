import sys


def menor_janela(valores, k):
    if k >= len(valores):
        soma = sum(valores)
        return (soma, 0)

    menor_soma = sum(valores[0:k])
    melhor_pos = 0

    for i in range(len(valores) - k + 1):
        janela = valores[i : i + k]
        soma_atual = sum(janela)

        if soma_atual < menor_soma:
            menor_soma = soma_atual
            melhor_pos = i

    return (menor_soma, melhor_pos)


# Estude a parte a seguir.
# Não modifique nada a partir daqui

if len(sys.argv) > 2:
    inputfile = sys.argv[1]
    janela = int(sys.argv[2])
    with open(inputfile, "r") as f:
        valores = list(map(int, f.read().split()))
        resultado = menor_janela(valores, janela)
        print(resultado)