import sys


def calcular(cedulas, valor):
    dp = [float("inf")] * (valor + 1)
    dp[0] = 0

    for i in range(1, valor + 1):
        for c in cedulas:
            if i - c >= 0:
                if dp[i - c] + 1 < dp[i]:
                    dp[i] = dp[i - c] + 1

    if dp[valor] == float("inf"):
        return -1

    return dp[valor]


# Estude a parte a seguir.
# Não modifique nada a partir daqui

def main(argv):
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
        with open(inputfile, "r") as f:
            valores = list(map(int, f.read().split()))
        print(calcular(valores[1:], valores[0]))

if __name__ == "__main__":
    main(sys.argv)