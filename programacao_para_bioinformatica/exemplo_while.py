continua_executando = True
print("O programa continuará executando até o usuário digitar n")
while(continua_executando):
    print("Winter is coming")
    continua_executando = ("n" != input("Deseja continuar executando? (s/n)").lower())
print("Programa finalizado")
