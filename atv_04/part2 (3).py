def caminho(labirinto, linha, coluna):
    if not labirinto:
        return None

    if isinstance(labirinto[0], str):
        labirinto = [list(l) for l in labirinto]

    if linha < 0 or linha >= len(labirinto) or coluna < 0 or coluna >= len(labirinto[0]):
        return None

    posicao_atual = labirinto[linha][coluna]

    if posicao_atual == '#' or posicao_atual == 'X':
        return None

    if posicao_atual == 'D':
        return [(linha, coluna)]

    caractere_antigo = labirinto[linha][coluna]
    labirinto[linha][coluna] = 'X'

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dl, dc in movimentos:
        resultado = caminho(labirinto, linha + dl, coluna + dc)
        if resultado is not None:
            labirinto[linha][coluna] = caractere_antigo
            return [(linha, coluna)] + resultado

    labirinto[linha][coluna] = caractere_antigo
    return None