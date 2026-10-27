import sys


def comprimir(valores):
    
    if len(valores) == 0:
        return []

    resp = []
    num_atual = valores[0]
    qtd = 1

    for i in range(1, len(valores)):
        if valores[i] == num_atual:
            qtd = qtd + 1
        else:
            resp.append((num_atual, qtd))
            num_atual = valores[i]
            qtd = 1

    resp.append((num_atual, qtd))

    return resp


def descomprimir(compactado):
    resp = []

    for item in compactado:
        val = item[0]
        qtd = item[1]

        for k in range(qtd):
            resp.append(val)

    return resp


# Estude a parte a seguir.
# Não modifique nada a partir daqui

if len(sys.argv) > 2:
    inputfile = sys.argv[1]
    tarefa = int(sys.argv[2])

    with open(inputfile, "r") as f:

        if tarefa == 0:
            valores = list(map(int, f.read().split()))
            resultado = comprimir(valores)

        elif tarefa == 1:
            compactado = []
            for linha in f:
                valor, quantidade = map(int, linha.split())
                compactado.append((valor, quantidade))
            resultado = descomprimir(compactado)

        print(resultado)