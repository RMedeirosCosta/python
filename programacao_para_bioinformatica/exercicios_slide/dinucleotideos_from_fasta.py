import re
from sys import argv

def imprimir(cabecalho, sequencia, dinucleotideos):
    print("\n"+cabecalho)
    for i in dinucleotideos[0]:
        for j in dinucleotideos[1]:
            print("Quantidade de " + str(i+j) + ":", sequencia.count(i+j))

def main():
    try:
        arquivo = open(argv[1], "r")
        
        # Separando apenas as sequências sem o cabeçalho
        sequencias = re.split(">.*\n", arquivo.read(), re.MULTILINE)

        # Voltando para início do arquivo
        arquivo.seek(0)

        # Lendo os cabeçalhos
        cabecalhos = re.findall(">.*\n", arquivo.read())

        # Removendo o primeiro índice vazio
        del sequencias[0]

        nucleotideos = ("A", "T", "G", "C")
        dinucleotideos = (nucleotideos, nucleotideos)
        validador = re.compile("^[ATGC]*$")

        # Limpando as quebras de linha e validando as sequências
        for i in range(len(cabecalhos)):
            sequencias[i] = re.sub("\n", "", sequencias[i])
            if (validador.match(sequencias[i]) is None):
                raise ValueError

            cabecalhos[i] = re.sub("[\n>]", "", cabecalhos[i])
            imprimir(cabecalhos[i], sequencias[i], dinucleotideos)

    except IOError:
        print("\nNão foi possível encontrar o arquivo " + argv[1] +". Verifique")
    except IndexError:
        print("\nInsira um parâmetro com o nome do arquivo. Por exemplo: python nucleotideos_from_file.py sequencia.fasta")
    except ValueError:
        print("\nO arquivo possui alguma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")

main()

