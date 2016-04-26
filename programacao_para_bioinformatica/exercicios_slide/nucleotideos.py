import re

def imprimir(sequencia, nucleotideo):
    print("Quantidade de " + str(nucleotideo) + ":", sequencia.count(nucleotideo))

def main():
    try:
        sequencia = input("Digite a sequência: ").upper()
        nucleotideos = ("A", "T", "G", "C")
        validador = re.compile("^[ATGC]*$")

        if (validador.match(sequencia) is None):
            raise ValueError

        print("\n-------RESULTADO------\n")

        for nucleotideo in nucleotideos:
            imprimir(sequencia, nucleotideo)
    except ValueError:
         print("Você digitou uma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
main()
