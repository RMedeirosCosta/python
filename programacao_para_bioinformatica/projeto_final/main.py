import re
from sys import argv
import pandas as pd
import numpy as np
from ggplot import *

def imprimir(sequencia, trinucleotideos):
    nt = {}
    dint = {}
    trint = {}
    
    for i in trinucleotideos[0]:
        nt[i] = [sequencia.count(i)]
        
        for j in trinucleotideos[1]:
            dint[i+j] = [sequencia.count(i+j)]
            
            for k in trinucleotideos[2]:
                trint[i+j+k] = [sequencia.count(i+j+k)]

    d = {}
    d.update(nt)
#    d.update(dint)
#    d.update(trint)
#    print(d)

    df = pd.DataFrame.from_dict(d)
    df = pd.melt(df)
    print(df)

    print(ggplot(aes(x='bn'), data=df) + geom_histogram())
    #print(ggplot(df, aes(x='pageviews')) + geom_histogram(binwidth=50))    
    #print(ggplot(aes(x='pageviews'), data=pageviews) + geom_histogram())

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
        trinucleotideos = (nucleotideos, nucleotideos, nucleotideos)
        validador = re.compile("^[ATGC]*$")

        # Limpando as quebras de linha e validando as sequências
        for i in range(len(cabecalhos)):
            sequencias[i] = re.sub("\n", "", sequencias[i])
            if (validador.match(sequencias[i]) is None):
                print(sequencias[i])
                raise ValueError

            cabecalhos[i] = re.sub("[\n>]", "", cabecalhos[i])
            imprimir(sequencias[i], trinucleotideos)

    except IOError:
        print("\nNão foi possível encontrar o arquivo " + argv[1] +". Verifique")
    except IndexError:
        print("\nInsira um parâmetro com o nome do arquivo. Por exemplo: python nucleotideos_from_file.py sequencia.fasta")
    except ValueError:
        print("\nO arquivo possui alguma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")

main()

