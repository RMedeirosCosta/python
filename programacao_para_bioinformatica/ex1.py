# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Exercicio 1
# Data: 22/03/2016
# Objetivo: Dados dois numeros naturais verificar quem e o maior
# Entrada: numero1, numero2 (inteiros)
# Saida: O numero maior
# Obs.: Verificar se a entrada e valida e depois retornar qual o maior numero

def main():
    try:
        numero1 = int(input("Digite o primeiro numero:"))

        if (numero1 < 0):
            raise ValueError
        
        numero2 = int(input("Digite o segundo numero:"))

        if (numero2 < 0):
            raise ValueError

        # Foram verificado pois ficava mais intuitivo

        CORPO_SAIDA = "O numero maior e: "

        if (numero1 > numero2):
            print(CORPO_SAIDA, numero1)
        elif (numero2 > numero1):
            print(CORPO_SAIDA, numero2)
        else:
            print("Os numeros sao iguais.")
        
    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um numero natural")
        main()

main()
