from random import randint
import random

def main():
    try:
        n = int(input("\nDigite um número natural n: "))

        if (n <= 0):
            raise ValueError
        
        per = float(input("Digite o % de Adenina ou Timina: "))        

        if ((per <= 0) | (per > 100)):
            raise ValueError

        quantidade_at = round(per*n/100)
        quantidade_cg = n-quantidade_at
        bases_nitrogenadas = ("A", "T", "C", "G")
        sequencia_aleatoria = ""
        
        for i in range(quantidade_at):
            sequencia_aleatoria += (bases_nitrogenadas[randint(0,1)])

        for i in range(quantidade_cg):
            sequencia_aleatoria += (bases_nitrogenadas[randint(2,3)])

        # Embaralhando a sequência
        temp_list = list(sequencia_aleatoria)
        random.shuffle(temp_list)
        sequencia_aleatoria = "".join(temp_list)
        
        print("\nSequência gerada: ", sequencia_aleatoria)
                                    
        f = open("sequencia.fasta", "w")
        f.write("> Arquivo FASTA gerado automaticamente\n")
        f.write(sequencia_aleatoria)
        f.close()
        
        print("\nArquivo sequencia.fasta gerado com sucesso")
        
    except ValueError:
        if (input("\nVocê digitou o número n ou o percentual AT inválido. Deseja continuar? (s/n)").lower() == "s"):
            main()
    
main()
