import re
from sys import argv

def imprimir(sequencia, dinucleotideo):
    print("Quantidade de " + str(dinucleotideo) + ":", sequencia.count(dinucleotideo))

def main():
    try:
        arquivo = open(argv[1], "r")
        sequencia = arquivo.read()
        nucleotideos = ("A", "T", "G", "C")
        dinucleotideos = (nucleotideos, nucleotideos)
        validador = re.compile("^[ATGC]*$")

        if (validador.match(sequencia) is None):
            raise ValueError

        print("\n-------RESULTADO------\n")

        for i in dinucleotideos[0]:
            for j in dinucleotideos[1]:
                imprimir(sequencia, (i+j))
            
    except IOError:
        print("\nNão foi possível encontrar o arquivo " + argv[1] +". Verifique\n")
    except IndexError:
        print("\nInsira um parâmetro com o nome do arquivo. Por exemplo: python nucleotideos_from_file.py sequencia.txt\n")
    except ValueError:
        print("\nO arquivo possui alguma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")

main()

