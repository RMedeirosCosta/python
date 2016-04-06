def smith_waterman(sequence1, sequence2):
    MATCH = 2
    MISMATCH = 1
    GAP = 2
    #    Inicializando a matriz
    n = len(sequence1)
    m = len(sequence2)
    matriz = [[0 for x in range(m)] for x in range(n)]

    x = 0
    for i in range(1, n):
        for j in range(1, m):

            if (sequence1[i-1] == sequence2[j-1]):
                x = matriz[i-1][j-1] + MATCH
            else:
                x = matriz[i-1][j-1] - MISMATCH

            if (x < (matriz[i-1][j] - GAP)):
                x = (matriz[i-1][j] - GAP)

            if (x < (matriz[i][j-1] - GAP)):
                x =  (matriz[i][j-1] - GAP)

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
