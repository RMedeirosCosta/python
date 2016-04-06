# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Mostrar Naturais
# Data: 02/04/2016
# Objetivo: Dado um numero natural, imprimir os n primeiros naturais até o número
# Entrada: numero (inteiro)
# Saida: Os numeros naturais ate numero digitado
# Obs.: Verificar se o numero e natural e depois imprimir naturais [1,N]

def obter_numeros(numero_maximo):
    numeros_impares = []
    
    for i in range(1, (numero_maximo+1)):
        numeros_impares.append(i)

    return numeros_impares

def main():
    try:
        numero = int(input("Digite um numero natural: "))
        
        if (numero < 0):
            raise ValueError

        # Foi utilizado uma lista para nao houver quebra de linha em cada numero
        print("Os numeros naturais de 1 a " + str(numero) + " sao:", obter_numeros(numero))        
    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um numero natural.")
        main()

main()
