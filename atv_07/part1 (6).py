def maior_janela(medicoes, limite, criterio):
    inicio = 0
    max_comprimento = 0
    minimo = -1
    maximo = -1
    n = len(medicoes)
    
    for fim in range(n):
        
        if not criterio(medicoes[fim]):
            inicio = fim + 1
            continue
            
        
        while inicio <= fim:
            subjanela = medicoes[inicio:fim + 1]
            if max(subjanela) - min(subjanela) <= limite:
                break
            inicio = inicio + 1
            
        
        if inicio <= fim:
            comprimento = fim - inicio + 1
            if comprimento > max_comprimento:
                max_comprimento = comprimento 
                minimo = inicio
                maximo = fim
                
    if max_comprimento == 0:
        return None  
        
    return (minimo, maximo)
