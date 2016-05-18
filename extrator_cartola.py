import re
from sys import argv
import sys

try:
    entrada = argv[1].strip()
    saida = argv[2].strip()
    f = open(entrada, 'r')
except:
    print("Houve um erro com os parametros de entrada.\n"+
          "Exemplo: python extrator_cartola.py arquivo_entrada arquivo_saida")
    sys.exit()

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

        
