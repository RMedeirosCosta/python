import re

def is_par(numero):
    return ((numero % 2)==0)

def main():
    try:
        entrada = input("Digite um número inteiro: ")
        validador = re.compile("^\d*$")

        if (validador.match(entrada) is None):
            raise ValueError

        resultado = "É par" if is_par(int(entrada)) else "É ímpar"
        print(resultado)

    except ValueError:
         print("Digite um número!")
         if (input("Desejar tentar novamente? (s/n): ").lower() == "s"):
             main()
main()

