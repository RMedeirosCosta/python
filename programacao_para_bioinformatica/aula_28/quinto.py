lista = [1,4,5,1,4,1]
conjunto = set(lista)

for i in conjunto:
    print(str(i)+": "+str(lista.count(i)))
