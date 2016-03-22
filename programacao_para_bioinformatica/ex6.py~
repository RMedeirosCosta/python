# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Exercicio 5
# Data: 22/03/2016
# Objetivo: Dado um numero natural de base binaria, transformalo para base decimal
# Entrada: numero (inteiro)
# Saida: O numero em base decimal
# Obs.: Verificar se o numero e natural e se e de base binaria e depois imprimir o numero convertido em base decimal

def is_binario(numero):
    for i in numero:
        if (i not in ['0','1']):
            return False

    return True

def converter_decimal(numero_binario):
    somatorio = 0
    expoentes = range((len(numero_binario)-1), -1, -1)
    
    for indice, unidade in enumerate(numero_binario):
        somatorio += (int(unidade) * (2**expoentes[indice]))

    return str(somatorio)

def main():
    try:
        numero = int(input("Digite um numero natural em base binaria: "))
        
        if (numero < 0):
            raise ValueError

        # Faco o casting para string para facilitar nas verificacoes
        numero_str = str(numero)

        if (not is_binario(numero_str)):
            raise ValueError

        print("O numero "+numero_str+" na base decimal e: "+converter_decimal(numero_str))

    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um numero natural de base binaria. Exp: 10110, 01, 10001110")
        main()

main()
