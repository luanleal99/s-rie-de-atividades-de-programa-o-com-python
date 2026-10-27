import struct
import sys


def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def dias_no_ano(ano):
    return 366 if eh_bissexto(ano) else 365


def temperatura_media(nome_arquivo, ano):
    fmt_cabecalho = "<IH"
    tam_cabecalho = struct.calcsize(fmt_cabecalho)

    fmt_registro = "<BBHIff"
    tam_registro = struct.calcsize(fmt_registro)

    with open(nome_arquivo, "rb") as f:
        # Lendo o cabecalho: num_estacoes (I) e ano_inicio (H)
        dados_cabecalho = f.read(tam_cabecalho)
        if not dados_cabecalho:
            return 0.0

        num_estacoes, ano_inicio = struct.unpack(fmt_cabecalho, dados_cabecalho)

        if ano < ano_inicio:
            return 0.0

        # Calculando o deslocamento (offset) em dias de ano_inicio ate o ano desejado
        dias_offset = 0
        for a in range(ano_inicio, ano):
            dias_offset += dias_no_ano(a)

        # Total de registros antes do ano desejado (dias de anos anteriores * estacoes)
        registros_anteriores = dias_offset * num_estacoes
        offset_bytes = tam_cabecalho + (registros_anteriores * tam_registro)

        # Posicionando o ponteiro de leitura direto no ano desejado usando seek
        f.seek(offset_bytes)

        dias_do_ano = dias_no_ano(ano)
        total_registros_ano = dias_do_ano * num_estacoes

        soma_temp = 0.0
        cont_registros = 0

        for _ in range(total_registros_ano):
            bytes_reg = f.read(tam_registro)
            if not bytes_reg or len(bytes_reg) < tam_registro:
                break

            # Registro: dia (B), mes (B), ano (H), id_estacao (I), temp (f), pressao (f)
            dados = struct.unpack(fmt_registro, bytes_reg)
            temp = dados[4]

            soma_temp += temp
            cont_registros += 1

        if cont_registros == 0:
            return 0.0

        return soma_temp / cont_registros


def main():
    if len(sys.argv) != 3:
        print("Uso: python part2.py <arquivo> <ano>")
        return

    nome_arquivo = sys.argv[1]
    ano = int(sys.argv[2])

    media = temperatura_media(nome_arquivo, ano)

    print(f"{media:.2f}")


if __name__ == "__main__":
    main()