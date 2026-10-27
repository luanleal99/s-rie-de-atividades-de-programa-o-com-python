
import sys
import struct

def analisar_turma(nome_arquivo):
    formato = "<30sff"
    tamanho = struct.calcsize(formato)

    maior_media = 0
    melhor_aluno = ''
    aprovados = 0

    with open (nome_arquivo, 'rb') as funcao:
        while dados := funcao.read(tamanho):
            if len(dados) < tamanho:
                break

            nome_b, n1, n2 = struct.unpack(formato, dados)
            nome = nome_b.decode('latin - 1').strip('\x00').strip()
            media = (n1 + n2)/2

            if media > maior_media:
                maior_media = media
                melhor_aluno = nome

            if media >= 6.0:
                aprovados = aprovados + 1

    return (melhor_aluno, aprovados,)


def main():
    if len(sys.argv) != 2:
        print("Uso: python part1.py <arquivo>")
        return

    nome_arquivo = sys.argv[1]

    resultado = analisar_turma(nome_arquivo)

    print(resultado)


if __name__ == "__main__":
    main()
