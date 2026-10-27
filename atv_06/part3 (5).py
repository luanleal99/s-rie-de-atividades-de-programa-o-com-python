def executar(estado, operacoes):
    estado_atual = list(estado)
    historico = []

    for op in operacoes:
        tipo = op.get("tipo")

        if tipo == "adicionar":
            pos = op["posicao"]
            txt = op["texto"]
            estado_atual.insert(pos, txt)
            historico.append({
                "tipo": "adicionar",
                "posicao": pos,
                "texto": txt
            })

        elif tipo == "remover":
            pos = op["posicao"]
            if 0 <= pos < len(estado_atual):
                removido = estado_atual.pop(pos)
                historico.append({
                    "tipo": "remover",
                    "posicao": pos,
                    "texto_anterior": removido
                })

        elif tipo == "substituir":
            pos = op["posicao"]
            txt = op["texto"]
            if 0 <= pos < len(estado_atual):
                antigo = estado_atual[pos]
                estado_atual[pos] = txt
                historico.append({
                    "tipo": "substituir",
                    "posicao": pos,
                    "texto": txt,
                    "texto_anterior": antigo
                })

    return estado_atual, historico


def desfazer(estado, historico):
    estado_atual = list(estado)

    for op in reversed(historico):
        tipo = op.get("tipo")

        if tipo == "adicionar":
            pos = op["posicao"]
            if 0 <= pos < len(estado_atual):
                estado_atual.pop(pos)

        elif tipo == "remover":
            pos = op["posicao"]
            txt = op["texto_anterior"]
            estado_atual.insert(pos, txt)

        elif tipo == "substituir":
            pos = op["posicao"]
            txt_antigo = op["texto_anterior"]
            if 0 <= pos < len(estado_atual):
                estado_atual[pos] = txt_antigo

    return estado_atual