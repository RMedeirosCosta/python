# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Exercicio 2
# Data: 22/03/2016
# Objetivo: Dados 4 notas, calcular a media aritimetica
# Entrada: numero1, numero2, numero3, numero4 (numeros reais)
# Saida: A media
# Obs.: Verificar se os quatro numeros sao numeros reais e depois mostrar a media aritimetica deles

def obter_entrada(qtd_notas):
    notas = []
    for i in range(qtd_notas):
        nota = float(input("Digite a " + str(i+1) + " nota: "))
        if (nota < 0):
            raise ValueError
        notas.append(nota)
    return notas

def calcular(notas):
    somatorio = 0.0
    for nota in notas:
        somatorio += nota
    return (somatorio / len(notas))

def main():
    try:
        print("A media e:", calcular(obter_entrada(qtd_notas=4)))
        
    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um real positivo.")
        main()

main()
