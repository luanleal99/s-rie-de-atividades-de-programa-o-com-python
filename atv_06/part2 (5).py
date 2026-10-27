def tamanho_total(diretorio):
    total = 0
    for filho in diretorio.get("filhos", []):
        if filho["tipo"] == "arquivo":
            total = total + filho["tamanho"]
        elif filho["tipo"] == "diretorio":
            total = total + tamanho_total(filho)
    return total


def buscar(diretorio, extensao):
    resultados = []
    for filho in diretorio.get("filhos", []):
        if filho["tipo"] == "arquivo":
            if filho["nome"].endswith("." + extensao) or filho["nome"].endswith(extensao):
                resultados.append(filho["nome"])
        elif filho["tipo"] == "diretorio":
            resultados.extend(buscar(filho, extensao))
    return resultados


def adicionar_arquivo(diretorio, caminho, nome, tamanho):
    if not caminho:
        novos_filhos = []
        for f in diretorio.get("filhos", []):
            novos_filhos.append(f)
        novos_filhos.append({
            "tipo": "arquivo",
            "nome": nome,
            "tamanho": tamanho
        })
        return {
            "tipo": "diretorio",
            "nome": diretorio["nome"],
            "filhos": novos_filhos
        }

    sub_alvo = caminho[0]
    resto_caminho = caminho[1:]
    novos_filhos = []
    encontrou = False

    for f in diretorio.get("filhos", []):
        if f["tipo"] == "diretorio" and f["nome"] == sub_alvo:
            encontrou = True
            novos_filhos.append(adicionar_arquivo(f, resto_caminho, nome, tamanho))
        else:
            novos_filhos.append(f)

    if not encontrou:
        novo_sub = {
            "tipo": "diretorio",
            "nome": sub_alvo,
            "filhos": []
        }
        novos_filhos.append(adicionar_arquivo(novo_sub, resto_caminho, nome, tamanho))

    return {
        "tipo": "diretorio",
        "nome": diretorio["nome"],
        "filhos": novos_filhos
    }


def remover_arquivo(diretorio, caminho):
    if not caminho:
        return diretorio

    alvo = caminho[0]
    resto_caminho = caminho[1:]

    novos_filhos = []
    for f in diretorio.get("filhos", []):
        if len(caminho) == 1:
            if f["nome"] == alvo:
                continue
            novos_filhos.append(f)
        else:
            if f["tipo"] == "diretorio" and f["nome"] == alvo:
                novos_filhos.append(remover_arquivo(f, resto_caminho))
            else:
                novos_filhos.append(f)

    return {
        "tipo": "diretorio",
        "nome": diretorio["nome"],
        "filhos": novos_filhos
    }