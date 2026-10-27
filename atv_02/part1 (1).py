import sys


def interpretar_comando(cmd):
    direcao = cmd[-1]
    quantidade = int(cmd[:-1])
    return quantidade, direcao


def mover(posicao, direcao):
    x, y = posicao
    if direcao == "N":
        return (x, y + 1)
    elif direcao == "S":
        return (x, y - 1)
    elif direcao == "L":
        return (x + 1, y)
    elif direcao == "O":
        return (x - 1, y)
    return posicao


def distancia_origem(posicao):
    x, y = posicao
    return x**2 + y**2


def executar(comandos):
    posicao_atual = (0, 0)
    maior_dist = 0

    for cmd in comandos:
        quantidade, direcao = interpretar_comando(cmd)

        for _ in range(quantidade):
            posicao_atual = mover(posicao_atual, direcao)
            dist = distancia_origem(posicao_atual)

            if dist > maior_dist:
                maior_dist = dist

    return (posicao_atual, maior_dist)


# Estude a parte a seguir.
# Não modifique nada a partir daqui

def main(argv):
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
        with open(inputfile, "r") as f:
            comandos = f.read().split()
            resultado = executar(comandos)        
            
            print(resultado)

if __name__ == "__main__":
    main(sys.argv)