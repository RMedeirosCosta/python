from random import randint

def main():
    try:
        n = int(input("\nDigite um número natural n: "))
        
        if (n <= 0):
            raise ValueError

        bases_nitrogenadas = ("A", "T", "C", "G")
        sequencia_aleatoria = ""
        
        for i in range(n):
            sequencia_aleatoria += (bases_nitrogenadas[randint(0,3)])
        print("\nSequência gerada: ", sequencia_aleatoria)
                                    
        f = open("sequencia.fasta", "w")
        f.write("> Arquivo FASTA gerado automaticamente\n")
        f.write(sequencia_aleatoria)
        f.close()
        
        print("\nArquivo sequencia.fasta gerado com sucesso")
        
    except ValueError:
        if (input("\nO número n precisa ser um número natural. Deseja continuar? (s/n)").lower() == "s"):
            main()
    
main()
