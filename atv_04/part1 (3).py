def primeira_ocorrencia(valores, valor, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if valores[meio] == valor:
        if meio == 0 or valores[meio - 1] != valor:
            return meio
        else:
            return primeira_ocorrencia(valores, valor, inicio, meio - 1)
    
    elif valores[meio] > valor:
        return primeira_ocorrencia(valores, valor, inicio, meio - 1)
    
    else:
        return primeira_ocorrencia(valores, valor, meio + 1, fim)