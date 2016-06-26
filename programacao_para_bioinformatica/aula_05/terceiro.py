import re
from sys import argv

def main():
    try:
        arquivo = open(argv[1], "r")
        validador = re.compile("^[ATGC]*$")
        sequencia = arquivo.read()
        
        if (validador.match(sequencia) is None):
            raise ValueError
        
        nucleotideos = {"G":sequencia.count("G"), "C":sequencia.count("C")}        

        print("Sequencia: "+sequencia+" %CG: ", round((nucleotideos["G"]+nucleotideos["C"])*100/len(sequencia),2))

    except IOError:
        print("\nNão foi possível encontrar o arquivo " + argv[1] +". Verifique")
    except IndexError:
        print("\nInsira um parâmetro com o nome do arquivo. Por exemplo: python nucleotideos_from_file.py sequencia.txt")
    except ValueError:
        print("\nO arquivo possui alguma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
        
main()

