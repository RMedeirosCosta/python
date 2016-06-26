import re

def main():
    try:
        sequencia = input("Digite a sequência: ").upper()

        validador = re.compile("^[ATGC]*$")

        if (validador.match(sequencia) is None):
            raise ValueError
        
        nucleotideos = {}
        nucleotideos["A"] = sequencia.count("A")
        nucleotideos["T"] = sequencia.count("T")
        nucleotideos["G"] = sequencia.count("G")
        nucleotideos["C"] = sequencia.count("C")
        
        print("\n-------RESULTADO------\n")
        print(nucleotideos)
    except ValueError:
         print("Você digitou uma sequência inválida. As sequências devem ter apenas caracteres ATGC sendo que a segunda deve ser apenas ATGC e ter apenas 3 bases.\n")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
main()
