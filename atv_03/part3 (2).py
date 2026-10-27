import struct
import sys

# Formatos explícitos com '<' para evitar padding inesperado
FMT_CABECALHO_FILME = "<i"  # 4 bytes: qtd_filmes
TAM_CABECALHO_FILME = 4

FMT_FILME = "<100si"  # 100 bytes nome + 4 bytes offset = 104 bytes
TAM_FILME = 104

FMT_AVALIACAO = "<iBi"  # 4 bytes id_user + 1 byte estrelas + 4 bytes prox_offset = 9 bytes
TAM_AVALIACAO = 9


def cadastrar_filme(nome_arquivo, nome):
    # Formata o nome para 100 bytes (preenche com bytes nulos se menor)
    nome_bytes = nome.encode("utf-8")
    if len(nome_bytes) > 100:
        nome_bytes = nome_bytes[:100]
    else:
        nome_bytes = nome_bytes.ljust(100, b"\x00")

    filmes = []

    try:
        with open(nome_arquivo, "rb") as f:
            dados_qtd = f.read(TAM_CABECALHO_FILME)
            if dados_qtd:
                qtd = struct.unpack(FMT_CABECALHO_FILME, dados_qtd)[0]
                for _ in range(qtd):
                    dados_f = f.read(TAM_FILME)
                    if len(dados_f) == TAM_FILME:
                        n_b, offset = struct.unpack(FMT_FILME, dados_f)
                        filmes.append((n_b, offset))
    except FileNotFoundError:
        pass

    # Adiciona o novo filme (offset inicial de avaliacoes = -1)
    filmes.append((nome_bytes, -1))

    # Ordena alfabeticamente considerando a string decodificada sem os bytes nulos
    filmes.sort(key=lambda x: x[0].decode("utf-8", errors="ignore").rstrip("\x00"))

    # Reescreve o arquivo atualizado
    with open(nome_arquivo, "wb") as f:
        f.write(struct.pack(FMT_CABECALHO_FILME, len(filmes)))
        for n_b, offset in filmes:
            f.write(struct.pack(FMT_FILME, n_b, offset))


def cadastrar_avaliacao(
    nome_arquivo, avaliacoes_arquivo, nome_filme, id_usuario, estrelas
):
    posicao_filme = -1
    offset_primeira_aval = -1

    # Busca o filme no arquivo principal
    with open(nome_arquivo, "rb+") as f:
        dados_qtd = f.read(TAM_CABECALHO_FILME)
        if not dados_qtd:
            return
        qtd = struct.unpack(FMT_CABECALHO_FILME, dados_qtd)[0]

        for i in range(qtd):
            pos_atual = f.tell()
            dados_f = f.read(TAM_FILME)
            if len(dados_f) < TAM_FILME:
                break
            n_b, offset = struct.unpack(FMT_FILME, dados_f)
            nome_str = n_b.decode("utf-8", errors="ignore").rstrip("\x00")

            if nome_str == nome_filme:
                posicao_filme = pos_atual
                offset_primeira_aval = offset
                break

        if posicao_filme == -1:
            return  # Filme nao encontrado

        # Escreve a nova avaliacao no final do arquivo de avaliacoes
        try:
            with open(avaliacoes_arquivo, "rb+") as f_aval:
                f_aval.seek(0, 2)  # Ir para o fim do arquivo
                novo_offset = f_aval.tell()
                nova_aval_bytes = struct.pack(
                    FMT_AVALIACAO, id_usuario, estrelas, -1
                )
                f_aval.write(nova_aval_bytes)
        except FileNotFoundError:
            with open(avaliacoes_arquivo, "wb") as f_aval:
                novo_offset = 0
                nova_aval_bytes = struct.pack(
                    FMT_AVALIACAO, id_usuario, estrelas, -1
                )
                f_aval.write(nova_aval_bytes)

        # Atualiza encadeamento de ponteiros/offsets
        if offset_primeira_aval == -1:
            # Era o primeiro registro, atualiza direto no filme
            f.seek(posicao_filme + 100)
            f.write(struct.pack("<i", novo_offset))
        else:
            # Percorre a lista encadeada ate o ultimo elemento
            with open(avaliacoes_arquivo, "rb+") as f_aval:
                atual = offset_primeira_aval
                while True:
                    f_aval.seek(atual)
                    dados_a = f_aval.read(TAM_AVALIACAO)
                    u_id, est, prox = struct.unpack(FMT_AVALIACAO, dados_a)

                    if prox == -1:
                        # Atualiza o prox do ultimo para o novo offset
                        f_aval.seek(atual + 5)  # 4 bytes (int) + 1 byte (char) = offset 5
                        f_aval.write(struct.pack("<i", novo_offset))
                        break
                    atual = prox


def somar_avaliacoes(nome_arquivo, avaliacoes_arquivo, nome_filme):
    offset_primeira = -1

    try:
        with open(nome_arquivo, "rb") as f:
            dados_qtd = f.read(TAM_CABECALHO_FILME)
            if not dados_qtd:
                return 0, 0
            qtd = struct.unpack(FMT_CABECALHO_FILME, dados_qtd)[0]

            for _ in range(qtd):
                dados_f = f.read(TAM_FILME)
                if len(dados_f) < TAM_FILME:
                    break
                n_b, offset = struct.unpack(FMT_FILME, dados_f)
                nome_str = n_b.decode("utf-8", errors="ignore").rstrip("\x00")

                if nome_str == nome_filme:
                    offset_primeira = offset
                    break
    except FileNotFoundError:
        return 0, 0

    if offset_primeira == -1:
        return 0, 0

    soma = 0
    qtd_avaliacoes = 0
    atual = offset_primeira

    try:
        with open(avaliacoes_arquivo, "rb") as f_aval:
            while atual != -1:
                f_aval.seek(atual)
                dados_a = f_aval.read(TAM_AVALIACAO)
                if len(dados_a) < TAM_AVALIACAO:
                    break

                u_id, estrelas, prox = struct.unpack(FMT_AVALIACAO, dados_a)
                soma += estrelas
                qtd_avaliacoes += 1
                atual = prox
    except FileNotFoundError:
        return 0, 0

    return soma, qtd_avaliacoes


if __name__ == "__main__":
    pass