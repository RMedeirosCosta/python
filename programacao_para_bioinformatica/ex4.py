# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Exercicio 4
# Data: 22/03/2016
# Objetivo: Dado um numero natural, imprimir os n primeiros naturais impares
# Entrada: numero (inteiro)
# Saida: Os numeros impares ate numero digitado
# Obs.: Verificar se o numero e natural e depois imprimir naturais impares [1,N]

def obter_numeros(numero_maximo):
    numeros_impares = []
    
    for i in range(1, (numero_maximo+1)):
        if ((i % 2) != 0):
            numeros_impares.append(i)

    return numeros_impares

def main():
    try:
        numero = int(input("Digite um numero natural: "))
        
        if (numero < 0):
            raise ValueError

        # Foi utilizado uma lista para nao houver quebra de linha em cada numero
        print("Os numeros impares de 1 a " + str(numero) + " sao:", obter_numeros(numero))        
    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um numero natural.")
        main()

main()
