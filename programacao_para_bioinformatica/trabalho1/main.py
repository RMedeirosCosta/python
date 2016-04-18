import re

def obter_antisense(sequencia):
    return sequencia.replace("A", "X").replace("T","A").replace("X","T").replace("G","X").replace("C","G").replace("X","C")

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

        print("Frame 1:", sequencia)
        print("Frame 2:", sequencia[1:])
        print("Frame 3:", sequencia[2:])
        print("Antisense:", obter_antisense(sequencia))

    except ValueError:
         print("Você digitou uma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
             
main()
