def smith_waterman(sequence1, sequence2):
    #    Inicializando a matriz
    n = len(sequence1)
    m = len(sequence2)
    matriz = [[0 for x in range(m)] for x in range(n)]
    print(matriz)

    x = 0
    for i in range(1, n):
        for j in range(1, m):
            print(matriz[i-1][j])
            if (sequence1[i-1] == sequence2[j-1]):
                x = matriz[i-1][j-1] + 2
            else:
                x = matriz[i-1][j-1] - 1

            if (x < (matriz[i-1][j] - 2)):
                x = (matriz[i-1][j] - 2)

            if (x < (matriz[i][j-1] - 2)):
                x =  (matriz[i][j-1] - 2)

            if (x < 0):
                x = 0

            matriz[i][j] = x

    score = matriz[n-1][m-1]
    
    for i in range(1, n):
        for j in range(1, m):
            if (score < matriz[i][j]):
                score = matriz[i][j]


    return score;
            

def main():
    SEQUENCE_1 = "AGTTGAAA"
    SEQUENCE_2 = "GGGTTATGGA"

    print(SEQUENCE_1, SEQUENCE_2, str(smith_waterman(SEQUENCE_1, SEQUENCE_2)))

main()
