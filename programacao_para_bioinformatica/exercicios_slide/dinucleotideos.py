import re

def imprimir(sequencia, dinucleotideo):
    print("Quantidade de " + str(dinucleotideo) + ":", sequencia.count(dinucleotideo))

def main():
    try:
        sequencia = input("Digite a sequência: ").upper()
        nucleotideos = ("A", "T", "G", "C")
        dinucleotideos = (nucleotideos, nucleotideos)
        validador = re.compile("^[ATGC]*$")

        if (validador.match(sequencia) is None):
            raise ValueError

        print("\n-------RESULTADO------\n")

        for i in dinucleotideos[0]:
            for j in dinucleotideos[1]:
                imprimir(sequencia, (i+j))
    except ValueError:
         print("Você digitou uma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
main()

