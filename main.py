from pessoa_service import listarPessoa, criarPessoa, atualizarPessoa, buscarPessoa, deletarPessoa

while True:
    print("\n1. - Criar pessoa")
    print("2. - Listar pessoas")
    print("3. - Deletar pessoa")
    print("4. - Atualizar pessoa")
    print("5. - Buscar pessoa")
    print("6. - Sair")
    opcao = input("Escolha :")

    if opcao == "1":
        nome = input("Digite o nome do pessoa: ")
        idade = int(input("Digite sua idade: "))
        email = input("Digite o email do pessoa: ")
        criarPessoa(nome, idade, email)
        print("Pessoa criada com sucesso!")


    elif opcao == "2":
        for p in listarPessoa():
            print(f"ID: {p['id']} | Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")

    elif opcao == "3":
        for p in listarPessoa():
            print(f"ID: {p['id']} | Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")

        idAlvo = int(input("\nSelecione o id da pessoa que será deletada:"))
        if deletarPessoa(idAlvo):
            print("Pessoa deletada com sucesso!")
        else:
            print("ID não encontrado.")

    elif opcao == "4":
        for p in listarPessoa():
            print(f"ID: {p['id']} | Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")

        print("\nInsira os novo campos da pessoa:")
        id = int(input("Digite o id do pessoa: "))
        nome = input("Digite o nome do pessoa: ")
        idade = int(input("Digite o idade do pessoa: "))
        email = input("Digite o email do pessoa: ")
        if atualizarPessoa(idAlvo, nome, idade, email):
            print("Pessoa atualizada com sucesso!")
        else:
            print("ID não encontrado.")

        buscarPessoa(id)
        print("Pessoa atualizada com sucesso!")

    elif opcao == "5":
        for p in listarPessoa():
            print(f"ID: {p['id']} | Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")

        idAlvo = int(input("Digite o id da pessoa que deseja buscar: "))
        p = buscarPessoa(idAlvo)
        if p is None:
            print("ID não encontrado.")
        else:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")

    elif opcao == "6":
        exit()





