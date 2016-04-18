import re

def imprimir(sequencia1, sequencia2, leitura, antisense=False):
    try:
        sequencia = sequencia1[(leitura-1):]
        leitura *= -1 if antisense else 1
        
        print("Leitura", leitura, sequencia,"Quantidade encontrado:", sequencia.count(sequencia2), "\nPosições: ", [(s+1) for s in [x.start() for x in re.finditer(sequencia2, sequencia)]])
    except:
        print("Leitura", leitura, sequencia,"Quantidade encontrado:", sequencia.count(sequencia2), "\nPosições: Não há ocorrência")
        
def obter_antisense(sequencia):
    return sequencia.replace("A", "X").replace("T","A").replace("X","T").replace("G","X").replace("C","G").replace("X","C")[::-1]

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
        for i in range(1,4):
            imprimir(sequencia, sequencia2, i)
        for i in range(1,4):
            imprimir(antisense, sequencia2, i, antisense=True)

    except ValueError:
         print("Você digitou uma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
             
main()
