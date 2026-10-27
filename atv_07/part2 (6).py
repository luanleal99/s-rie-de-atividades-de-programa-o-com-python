def criar_politica_peso_maximo(limite):
    def politica(lote):
        for peso in lote:
            if peso > limite:
                return False
        return True
    return politica

def organizar_pacotes(pesos, capacidade, max_pacotes, politica):
    memo = {}

    def resolver(indice):
        if indice == len(pesos):
            return []
        
        if indice in memo:
            return memo[indice]
        
        melhor_solucao = None
        
        for k in range(1, max_pacotes + 1):
            if indice + k > len(pesos):
                break
                
            sub_pesos = pesos[indice:indice + k]
            
            if sum(sub_pesos) <= capacidade and politica(sub_pesos):
                indices_lote = list(range(indice, indice + k))
                
                restante = resolver(indice + k)
                
                if restante is not None:
                    candidato = [indices_lote] + restante
                    
                    if melhor_solucao is None or len(candidato) < len(melhor_solucao):
                        melhor_solucao = candidato
                        
        memo[indice] = melhor_solucao
        return melhor_solucao

    return resolver(0)