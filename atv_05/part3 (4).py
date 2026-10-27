
import sys
import ast

def achatar_lista(dados):
    resultado = []
    for item in dados:
        if isinstance(item, list):
            # Chamada recursiva para sublista
            sublista = achatar_lista(item)
            for x in sublista:
                resultado.append(x)
        else:
            resultado.append(item)
    return resultado

# NAO MODIFIQUE NADA A PARTIR DAQUI

def main(argv):
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
        with open(inputfile, "r") as f:
            linhas = f.read().splitlines()
            
            for linha in linhas:
                if not linha.strip():
                    continue
                
                # ast.literal_eval converte a string do txt em uma lista python real
                dados = ast.literal_eval(linha.strip())
                resultado = achatar_lista(dados)
                print(resultado)

if __name__ == "__main__":
    main(sys.argv)