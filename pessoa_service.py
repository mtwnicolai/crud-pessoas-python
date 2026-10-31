from storage import carregar, salvar

def listarPessoa():
    pessoas = carregar()
    return pessoas

def criarPessoa(nome, idade, email):  # Define a função
    pessoas = carregar()  # Lê o json data/pessoas.json

    if len(pessoas) == 0:  # Se a lista estiver vazia
        novo_id = 1  # o primeiro é id "1"
    else: # Senão
        novo_id = max(p["id"] for p in pessoas)+1  # Pega o id maior e soma "+1"

    pessoa = {"id": novo_id, "nome": nome, "idade": idade, "email": email}  # Monta a "ficha" da pessoa

    pessoas.append(pessoa)  # Coloca na lista
    salvar(pessoas)  # Salva no arquivo certo
    return pessoas

def deletarPessoa(id):
    pessoas = carregar()
    tamanhoAntes = len(pessoas)

    pessoas = [p for p in pessoas if p["id"] != id]

    if len(pessoas) == tamanhoAntes:
        return False

    salvar(pessoas)
    return True

if __name__ == "__main__":

    print(listarPessoa())
