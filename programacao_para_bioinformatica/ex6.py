# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Exercicio 6
# Data: 22/03/2016
# Objetivo: Dado um numero natural maior que 10, verificar se o numero e palindromo
# Entrada: numero (inteiro)
# Saida: resposta se o numero e palindromo ou nao
# Obs.: Verificar se o numero e natural maior que 10 e depois informar se e palindromo ou nao. Por definicao, todo numero palindromo e igual ao seu reverso

def main():
    try:
        # Converto para verificar se e int, se nao for e levantado uma excecao
        numero = int(input("Digite um numero natural maior que 10 "))
        
        if (numero <= 10):
            raise ValueError

        # Faco o casting para string para facilitar nas verificacoes
        numero_str = str(numero)
        reverso_numero = numero_str[::-1]

        resposta = " e " if (numero_str == reverso_numero) else " nao e "

        print("O numero "+numero_str+resposta+"palindromo")

    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um numero natural maior que 10.")
        main()

main()
