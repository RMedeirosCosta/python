import re
from sys import argv
import sys

def extrair(entrada, saida):
    f = open(entrada, 'r')

    planilha = []
    linha = ""
    for line in f:
        if ((line.strip() != "vender") and (line.strip() != "comprar")):
            linha += line.strip()+","
        else:
            linha = re.sub(r"C\$","",linha)
            planilha.append(linha)
            linha = ""
    f.close()
    f2 = open(saida, "w")
    f2.write("Nome,Clube,Sigla,Nome,Posicao,Ult,Media,Jogos,Lixo1,Lixo2,Lixo3,Preco,Valorizacao,\n")
    for l in planilha:
        f2.write(l+"\n")
    f2.close()

def main(entrada="",saida=""):
    try:
        if (entrada == ""):
            entrada = argv[1].strip()
        if (saida == ""):
            saida =  argv[2].strip()
        extrair(entrada, saida)
    except:
        print("Houve um erro com os parametros.\n"+
              "Exemplo: extrator_cartola.py arquivo_entrada arquivo_saida")
        if (input("Deseja continuar? (s/n) ").lower() == "s"):
            entrada = input("Digite o arquivo de entrada: ")
            saida = input("Digite o arquivo de saida: ")
            main(entrada, saida)

main()

        


        
