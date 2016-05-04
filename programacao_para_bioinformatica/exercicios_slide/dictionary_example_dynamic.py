def main():
    pessoa = {"nome":"Ricardo", "idade":23}
    print(pessoa["nome"])
    print(pessoa["idade"])

    pessoa["cidade"] = "Santo Antônio da Platina"
    print("Adicionado em tempo de execução CIDADE: ", pessoa["cidade"])
    
main()

