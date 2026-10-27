def ajuda_soma(valores, alvo, indice, atual_soma, solucao_atual):
    if atual_soma == alvo:
        return solucao_atual
    
    if atual_soma > alvo or indice >= len(valores):
        return None
    
    com_elem = ajuda_soma(valores, alvo, indice + 1, atual_soma + valores[indice], solucao_atual + [indice])
    if com_elem is not None:
        return com_elem
    
    sem_elem = ajuda_soma(valores, alvo, indice + 1, atual_soma, solucao_atual)
    if sem_elem is not None:
        return sem_elem
    
    return None


def encontrar_soma(valores, alvo):
    return ajuda_soma(valores, alvo, 0, 0, [])