def aplicar_operacoes(estado, operacoes):
    novo_usuarios = dict(estado["usuarios"])

    for op in operacoes:
        tipo = op.get("tipo")
        uid = op.get("usuario")

        if uid not in novo_usuarios:
            continue

        usuario = novo_usuarios[uid]
        valor = op.get("valor", 0)

        if tipo == "adicionar_pontos":
            if valor < 0 or not usuario["ativo"]:
                continue
            novo_usuarios[uid] = {
                "nome": usuario["nome"],
                "ativo": usuario["ativo"],
                "pontos": usuario["pontos"] + valor
            }

        elif tipo == "remover_pontos":
            if valor < 0 or not usuario["ativo"] or valor > usuario["pontos"]:
                continue
            novo_usuarios[uid] = {
                "nome": usuario["nome"],
                "ativo": usuario["ativo"],
                "pontos": usuario["pontos"] - valor
            }

        elif tipo == "ativar":
            if not usuario["ativo"]:
                novo_usuarios[uid] = {
                    "nome": usuario["nome"],
                    "ativo": True,
                    "pontos": usuario["pontos"]
                }

        elif tipo == "desativar":
            if usuario["ativo"]:
                novo_usuarios[uid] = {
                    "nome": usuario["nome"],
                    "ativo": False,
                    "pontos": usuario["pontos"]
                }

    return {"usuarios": novo_usuarios}