
def criar_filtro_distancia(minima, maxima):
    def filtro(corrida):
        distancia = corrida[1]
        if minima <= distancia <= maxima:
            return True
        return False
    return filtro


def criar_filtro_avaliacao(minima):
    def filtro(corrida):
        avaliacao = corrida[3]
        if avaliacao >= minima:
            return True
        return False
    return filtro


def criar_filtro_categoria(categoria):
    def filtro(corrida):
        cat = corrida[4]
        if cat == categoria:
            return True
        return False
    return filtro


def negar(filtro):
    def novo_filtro(corrida):
        if filtro(corrida):
            return False
        return True
    return novo_filtro


def combinar(filtros):
    def novo_filtro(corrida):
        for f in filtros:
            if not f(corrida):
                return False
        return True
    return novo_filtro


def consultar(nome_arquivo, filtro):
    resultado = []
    with open(nome_arquivo, 'r') as arq:
        for linha in arq:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(';')
            
            # Convertendo os campos da corrida
            nome = partes[0].strip()
            distancia = float(partes[1])
            duracao = int(partes[2])
            avaliacao = float(partes[3])
            categoria = partes[4].strip()
            
            corrida = (nome, distancia, duracao, avaliacao, categoria)
            
            if filtro(corrida):
                resultado.append(corrida)
                
    return resultado


if __name__ == "__main__":
    pass