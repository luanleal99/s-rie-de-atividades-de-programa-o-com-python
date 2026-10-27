def criar_politica_beneficio_minimo(limite):
    def politica(ponto):
        return ponto[1] >= limite
    return politica


def planejar_rota(pontos, orcamento, politica):
    memo = {}

    def resolver(i, orc_disp):
        if i >= len(pontos):
            return (0, 0, [])  # (beneficio, custo, indices)

        chave = (i, orc_disp)
        if chave in memo:
            return memo[chave]

        # Opção 1: Não visitar o ponto i
        ben1, custo1, indices1 = resolver(i + 1, orc_disp)

        # Opção 2: Visitar o ponto i (se for válido e couber no orçamento)
        custo, beneficio, classificacao = pontos[i]

        ben2, custo2, indices2 = -1, -1, None
        if custo <= orc_disp and politica(pontos[i]):
            b_rest, c_rest, ind_rest = resolver(i + 2, orc_disp - custo)
            if ind_rest is not None:
                ben2 = beneficio + b_rest
                custo2 = custo + c_rest
                indices2 = [i] + ind_rest

        # Escolhe a melhor opção
        if indices2 is None and indices1 is None:
            melhor = (-1, -1, None)
        elif indices2 is None:
            melhor = (ben1, custo1, indices1)
        elif indices1 is None:
            melhor = (ben2, custo2, indices2)
        else:
            if ben2 > ben1:
                melhor = (ben2, custo2, indices2)
            elif ben1 > ben2:
                melhor = (ben1, custo1, indices1)
            else:
                if custo2 < custo1:
                    melhor = (ben2, custo2, indices2)
                elif custo1 < custo2:
                    melhor = (ben1, custo1, indices1)
                else:
                    if indices2 < indices1:
                        melhor = (ben2, custo2, indices2)
                    else:
                        melhor = (ben1, custo1, indices1)

        memo[chave] = melhor
        return melhor

    ben, custo, resultado = resolver(0, orcamento)

    # Se a lista retornada for vazia (nenhum ponto pôde ser selecionado/comprado),
    # o enunciado exige retornar None
    if resultado is None or len(resultado) == 0:
        return None

    return resultado