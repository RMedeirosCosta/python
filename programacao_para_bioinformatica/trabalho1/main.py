import re

def imprimir(sequencia1, sequencia2, leitura, antisense=False):
    i = leitura
    sequencia_dividida = dividir(sequencia1[(i-1)::])
    
    if antisense:
        sequencia2 = sequencia2[::-1]
        leitura *= -1
        print("Leitura", leitura, sequencia_dividida,"Quantidade(s) encontrada(s):", sequencia_dividida.count(sequencia2), "\nPosições:",  [(idx*3+1) for idx, x in enumerate(sequencia_dividida) if (x == sequencia2)])
    else:
        print("Leitura", leitura, sequencia_dividida,"Quantidade(s) encontrada(s):", sequencia_dividida.count(sequencia2), "\nPosições:",  [(idx*3+1) for idx, x in enumerate(sequencia_dividida) if (x == sequencia2)])
        
def obter_antisense(sequencia):
    return sequencia.replace("A", "X").replace("T","A").replace("X","T").replace("G","X").replace("C","G").replace("X","C")

def dividir(sequencia):
    return [sequencia[i:i+3] for i in range(0, (len(sequencia)-2), 3)]

def main():
    try:         
        sequencia = input("Digite a sequência: ").upper()
        validador = re.compile("^[ATGC]*$")

        if (validador.match(sequencia) is None):
            raise ValueError

        sequencia2 = input("Digite a segunda sequência com apenas 3 bases. Exemplo: GCA\n").upper()
        validador = re.compile("^[ATGC]{3}$")

        if (validador.match(sequencia2) is None):
            raise ValueError

        antisense = obter_antisense(sequencia)
        print("\n\nProcura:", sequencia2)
        print("\nSense:     --------------------------> (+)");
        print(sequencia)
        for i in range(1,4):
            imprimir(sequencia, sequencia2, i)

        print("\nAntisense: <-------------------------- (-)")
        print(antisense)
        for i in range(1,4):
            imprimir(antisense, sequencia2, i, antisense=True)

    except ValueError:
         print("Você digitou uma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
             
main()
#s = "ATCGATCGA"
#print(s)
#print(dividir(s[len(s)::-1]))
#print(s[::-1])
#print(s[len(s)-2::-1])
#print(s[len(s)-3::-1])
#print(dividir(s[len(s)-1::-1]))
#print(dividir(s[len(s)-2::-1]))

      
      
