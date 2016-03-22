# Autor: Ricardo Medeiros da Costa Junior
# Titulo: Exercicio 3
# Data: 22/03/2016
# Objetivo: Dados 3 notas, calcular a media ponderada, sendo Nota 1 peso 2, nota 2 peso 5 e nota 3 peso 3.
# Entrada: nota1, nota2, nota3 (numeros reais)
# Saida: A media ponderada
# Obs.: Verificar se os 3 numeros sao numeros reais e depois mostrar a media ponderada deles

def obter_entrada(qtd_notas):
    notas = []

    # Criado apenas para duplicar o input
    for i in range(qtd_notas):
        nota = float(input("Digite a " + str(i+1) + " nota: "))
        if (nota < 0):
            raise ValueError
        notas.append(nota)
        
    notas_com_pesos = {2:notas[0], 5:notas[1], 3:notas[2]}
    return notas_com_pesos

def calcular(notas):
    somatorio_notas = 0.0
    somatorio_pesos = 0
    for peso in notas.keys():
        somatorio_notas += (peso * notas[peso])
        somatorio_pesos += peso
    return (somatorio_notas / somatorio_pesos)

def main():
    try:
        print("A media ponderada e:", calcular(obter_entrada(qtd_notas=3)))
        
    except ValueError:
        print("Numero invalido. Programa sera reiniciado. POR FAVOR! \n"
              "Informe um real positivo.")
        main()

main()
