palavra = input("Digite uma palavra: ")
n = len(palavra)-1
reverso = ""
while(n != 0):
    reverso = reverso + palavra[n]
    n = n-1
print(reverso)
