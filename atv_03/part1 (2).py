# Exercicio 1 - Gerador de Consultas


def criar_filtro_temperatura(minima, maxima):
    def filtro(medicao):
        # medicao eh uma tupla: (sensor, temp, pressao)
        temp = medicao[1]
        return minima <= temp <= maxima

    return filtro


def criar_filtro_pressao(minima, maxima):
    def filtro(medicao):
        pressao = medicao[2]
        return minima <= pressao <= maxima

    return filtro


def criar_filtro_sensor(sensor):
    def filtro(medicao):
        nome_sensor = medicao[0]
        return nome_sensor == sensor

    return filtro


def combinar(filtros):
    def filtro_composto(medicao):
        for f in filtros:
            if not f(medicao):
                return False
        return True

    return filtro_composto


def consultar(nome_arquivo, filtro):
    resultados = []

    with open(nome_arquivo, "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue

            # tratando a linha separando por ponto e virgula ou dois pontos
            # dependendo de como o arquivo veio formatado
            linha = linha.replace(":", ";")
            partes = linha.split(";")

            sensor = partes[0]
            temp = float(partes[1])
            pressao = float(partes[2])

            medicao = (sensor, temp, pressao)

            if filtro(medicao):
                resultados.append(medicao)

    return resultados


if __name__ == "__main__":
    pass
