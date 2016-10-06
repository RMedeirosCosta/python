import re
from sys import argv
import random

def main():
    EXEMPLO = "Exemplo: python gerador_pesquisa.py 200\n"
    
    try:        
        disciplinas = ("História", "Geografia", "Ensino Religioso", "Matemática", "Português", "Artes", "Educação Física", "Ciências")
        validador = re.compile("^\d+$")
        if (validador.match(argv[1]) is None):
            raise ValueError
        
        qtd_entrevistados = int(argv[1])
        respostas = []

        for i in range(qtd_entrevistados):
            respostas.append(disciplinas[random.randint(0,len(disciplinas)-1)])
            print("Aluno "+str(i+1)+" escolheu "+respostas[i])

        print("\n\nDistribuição de Frequências\n")
        print("Disciplina | Frequência Simples | Frequência Relativa | Frequência Simples Acumulada | Frequência Relativa Acumulada \n\n")
        
        freq_simples_acumulada = 0
        freq_relativa_acumulada = 0
        
        for i in range(len(disciplinas)):
            freq_simples = respostas.count(disciplinas[i])
            freq_simples_acumulada += freq_simples
            freq_relativa = freq_simples/qtd_entrevistados*100
            freq_relativa_acumulada += freq_relativa
            
            print(disciplinas[i]+" "+ str(freq_simples)+ " "+ "{0:.2f}".format(freq_relativa) + "% " + str(freq_simples_acumulada) + " " + "{0:.2f}".format(freq_relativa_acumulada)+"%")

    except IndexError:
        print("\nInsira um parâmetro. "+EXEMPLO)
    except ValueError:
        print("\nParâmetro inválido. "+EXEMPLO)

main()

