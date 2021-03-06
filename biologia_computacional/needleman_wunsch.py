def needleman_wunsch(sequence1, sequence2):
    GAP = -1
    MISMATCH = -1
    MATCH = 2

    #    Inicializando a matriz
    n = len(sequence1)
    m = len(sequence2)
    matriz = [[0 for x in range(m)] for x in range(n)]

    # Preenchendo os gaps
    for i in range(1, n):
        matriz[i][0] = i * GAP

    for j in range(1, m):
        matriz[0][j] = j * GAP

    x = 0
    for i in range(1, n):
        for j in range(1, m):

            if (sequence1[i-1] == sequence2[j-1]):
                x = matriz[i-1][j-1] + MATCH
            else:
                x = matriz[i-1][j-1] + MISMATCH

            if ((matriz[i-1][j] + GAP) > x):
                x = (matriz[i-1][j] + GAP)

            if ((matriz[1][j-1] + GAP) > x):
                x = (matriz[1][j-1] + GAP)

            matriz[i][j] = x

    score = matriz[n-1][m-1]
    return score

def main():
    SEQUENCE_1 = "ACGTA"
    SEQUENCE_2 = "CGTA"
    print("SCORE = " + str(needleman_wunsch(SEQUENCE_1, SEQUENCE_2)))
    
main()            
        
